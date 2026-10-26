#include "stm32f1xx_hal.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "odrive_can.h"

CAN_HandleTypeDef hcan;
SPI_HandleTypeDef hspi1;
UART_HandleTypeDef huart1;

enum {
    HOST_NOP = 0,
    HOST_MOVE_POSITION = 1,
    HOST_ENABLE = 2,
    HOST_IDLE = 3,
    HOST_ESTOP = 4,
    HOST_CLEAR_ERRORS = 5,
};

typedef struct __attribute__((packed)) {
    uint8_t magic;
    uint8_t command;
    uint8_t motor;
    uint8_t sequence;
    float position_turns;
    float velocity_ff_turns_s;
    float torque_ff_nm;
    uint8_t reserved[8];
} HostRequest;

typedef struct __attribute__((packed)) {
    uint8_t magic;
    uint8_t status;
    uint8_t last_command;
    uint8_t sequence;
    float position_turns[2];
    float velocity_turns_s[2];
    uint32_t combined_axis_error;
} HostResponse;

_Static_assert(sizeof(HostRequest) == 24, "HostRequest must be 24 bytes");
_Static_assert(sizeof(HostResponse) == 24, "HostResponse must be 24 bytes");

static uint8_t spi_rx[sizeof(HostRequest)];
static uint8_t spi_tx[sizeof(HostResponse)];
static volatile uint8_t command_ready;
static HostRequest pending_command;
static uint8_t last_status;

static void SystemClock_Config(void);
static void GPIO_Init(void);
static void CAN_Init(void);
static void SPI1_Init(void);
static void UART1_Init(void);
static void Error_Handler(void);

static void uart_write(const char *text) {
    HAL_UART_Transmit(&huart1, (uint8_t *)text, (uint16_t)strlen(text), 100);
}

static bool valid_motor(uint8_t motor) {
    return motor < ODRIVE_COUNT;
}

static uint8_t execute_command(const HostRequest *request) {
    bool ok = false;
    if (request == NULL || request->magic != 0xA5U) return 1;

    switch (request->command) {
        case HOST_NOP: return 0;
        case HOST_MOVE_POSITION:
            if (!valid_motor(request->motor)) return 2;
            ok = odrive_set_position(request->motor, request->position_turns,
                                     request->velocity_ff_turns_s,
                                     request->torque_ff_nm);
            break;
        case HOST_ENABLE:
            if (!valid_motor(request->motor)) return 2;
            ok = odrive_enable_position_control(request->motor);
            break;
        case HOST_IDLE:
            if (!valid_motor(request->motor)) return 2;
            ok = odrive_set_idle(request->motor);
            break;
        case HOST_ESTOP:
            ok = odrive_estop_all();
            break;
        case HOST_CLEAR_ERRORS:
            if (!valid_motor(request->motor)) return 2;
            ok = odrive_clear_errors(request->motor);
            break;
        default: return 3;
    }
    return ok ? 0 : 4;
}

static void prepare_response(uint8_t command, uint8_t sequence) {
    HostResponse response = {0};
    response.magic = 0x5AU;
    response.status = last_status;
    response.last_command = command;
    response.sequence = sequence;
    for (uint8_t node = 0; node < ODRIVE_COUNT; ++node) {
        const ODriveFeedback *value = odrive_feedback(node);
        response.position_turns[node] = value->position_turns;
        response.velocity_turns_s[node] = value->velocity_turns_s;
        response.combined_axis_error |= value->axis_error;
    }
    memcpy(spi_tx, &response, sizeof(response));
}

static void poll_uart(void) {
    static char line[64];
    static size_t length;
    uint8_t byte;
    if (HAL_UART_Receive(&huart1, &byte, 1, 0) != HAL_OK) return;

    if (byte == '\r' || byte == '\n') {
        line[length] = '\0';
        unsigned motor;
        float position;
        if (sscanf(line, "p %u %f", &motor, &position) == 2 && motor < ODRIVE_COUNT) {
            odrive_set_position((uint8_t)motor, position, 0.0f, 0.0f);
        } else if (sscanf(line, "enable %u", &motor) == 1 && motor < ODRIVE_COUNT) {
            odrive_enable_position_control((uint8_t)motor);
        } else if (sscanf(line, "idle %u", &motor) == 1 && motor < ODRIVE_COUNT) {
            odrive_set_idle((uint8_t)motor);
        } else if (sscanf(line, "clear %u", &motor) == 1 && motor < ODRIVE_COUNT) {
            odrive_clear_errors((uint8_t)motor);
        } else if (strcmp(line, "estop") == 0) {
            odrive_estop_all();
        } else if (length != 0U) {
            uart_write("Commands: p <0|1> <turns>, enable <0|1>, idle <0|1>, clear <0|1>, estop\r\n");
        }
        length = 0;
    } else if (length < sizeof(line) - 1U) {
        line[length++] = (char)byte;
    }
}

int main(void) {
    HAL_Init();
    SystemClock_Config();
    GPIO_Init();
    CAN_Init();
    SPI1_Init();
    UART1_Init();

    CAN_FilterTypeDef filter = {0};
    filter.FilterBank = 0;
    filter.FilterMode = CAN_FILTERMODE_IDMASK;
    filter.FilterScale = CAN_FILTERSCALE_32BIT;
    filter.FilterIdHigh = 0;
    filter.FilterIdLow = 0;
    filter.FilterMaskIdHigh = 0;
    filter.FilterMaskIdLow = 0;
    filter.FilterFIFOAssignment = CAN_RX_FIFO0;
    filter.FilterActivation = ENABLE;
    if (HAL_CAN_ConfigFilter(&hcan, &filter) != HAL_OK ||
        HAL_CAN_Start(&hcan) != HAL_OK ||
        HAL_CAN_ActivateNotification(&hcan, CAN_IT_RX_FIFO0_MSG_PENDING) != HAL_OK) {
        Error_Handler();
    }

    odrive_can_init(&hcan);
    prepare_response(HOST_NOP, 0);
    if (HAL_SPI_TransmitReceive_IT(&hspi1, spi_tx, spi_rx, sizeof(spi_rx)) != HAL_OK) {
        Error_Handler();
    }
    uart_write("Humanoid ankle controller ready; motors remain idle until enabled.\r\n");

    while (1) {
        if (command_ready != 0U) {
            HostRequest command;
            __disable_irq();
            memcpy(&command, &pending_command, sizeof(command));
            command_ready = 0;
            __enable_irq();
            if (command.command != HOST_NOP) {
                last_status = execute_command(&command);
                prepare_response(command.command, command.sequence);
            }
        }
        poll_uart();
    }
}

void HAL_CAN_RxFifo0MsgPendingCallback(CAN_HandleTypeDef *handle) {
    CAN_RxHeaderTypeDef header;
    uint8_t data[8];
    if (handle->Instance == CAN1 &&
        HAL_CAN_GetRxMessage(handle, CAN_RX_FIFO0, &header, data) == HAL_OK) {
        odrive_process_rx(&header, data);
    }
}

void HAL_SPI_TxRxCpltCallback(SPI_HandleTypeDef *handle) {
    if (handle->Instance != SPI1) return;
    if (command_ready == 0U) {
        memcpy(&pending_command, spi_rx, sizeof(pending_command));
        command_ready = 1U;
    }
    HAL_SPI_TransmitReceive_IT(&hspi1, spi_tx, spi_rx, sizeof(spi_rx));
}

void USB_LP_CAN1_RX0_IRQHandler(void) { HAL_CAN_IRQHandler(&hcan); }
void SPI1_IRQHandler(void) { HAL_SPI_IRQHandler(&hspi1); }

static void SystemClock_Config(void) {
    RCC_OscInitTypeDef oscillator = {0};
    RCC_ClkInitTypeDef clock = {0};
    oscillator.OscillatorType = RCC_OSCILLATORTYPE_HSE;
    oscillator.HSEState = RCC_HSE_ON;
    oscillator.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
    oscillator.PLL.PLLState = RCC_PLL_ON;
    oscillator.PLL.PLLSource = RCC_PLLSOURCE_HSE;
    oscillator.PLL.PLLMUL = RCC_PLL_MUL9;
    if (HAL_RCC_OscConfig(&oscillator) != HAL_OK) Error_Handler();

    clock.ClockType = RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_SYSCLK |
                      RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;
    clock.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
    clock.AHBCLKDivider = RCC_SYSCLK_DIV1;
    clock.APB1CLKDivider = RCC_HCLK_DIV2;
    clock.APB2CLKDivider = RCC_HCLK_DIV1;
    if (HAL_RCC_ClockConfig(&clock, FLASH_LATENCY_2) != HAL_OK) Error_Handler();
}

static void GPIO_Init(void) {
    __HAL_RCC_AFIO_CLK_ENABLE();
    __HAL_RCC_GPIOA_CLK_ENABLE();
    __HAL_AFIO_REMAP_SWJ_NOJTAG();
}

static void CAN_Init(void) {
    __HAL_RCC_CAN1_CLK_ENABLE();
    GPIO_InitTypeDef gpio = {0};
    gpio.Pin = GPIO_PIN_11;
    gpio.Mode = GPIO_MODE_INPUT;
    gpio.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &gpio);
    gpio.Pin = GPIO_PIN_12;
    gpio.Mode = GPIO_MODE_AF_PP;
    gpio.Speed = GPIO_SPEED_FREQ_HIGH;
    HAL_GPIO_Init(GPIOA, &gpio);

    hcan.Instance = CAN1;
    hcan.Init.Prescaler = 9;
    hcan.Init.Mode = CAN_MODE_NORMAL;
    hcan.Init.SyncJumpWidth = CAN_SJW_1TQ;
    hcan.Init.TimeSeg1 = CAN_BS1_6TQ;
    hcan.Init.TimeSeg2 = CAN_BS2_1TQ;
    hcan.Init.TimeTriggeredMode = DISABLE;
    hcan.Init.AutoBusOff = ENABLE;
    hcan.Init.AutoWakeUp = DISABLE;
    hcan.Init.AutoRetransmission = ENABLE;
    hcan.Init.ReceiveFifoLocked = DISABLE;
    hcan.Init.TransmitFifoPriority = DISABLE;
    if (HAL_CAN_Init(&hcan) != HAL_OK) Error_Handler();
    HAL_NVIC_SetPriority(USB_LP_CAN1_RX0_IRQn, 1, 0);
    HAL_NVIC_EnableIRQ(USB_LP_CAN1_RX0_IRQn);
}

static void SPI1_Init(void) {
    __HAL_RCC_SPI1_CLK_ENABLE();
    GPIO_InitTypeDef gpio = {0};
    gpio.Pin = GPIO_PIN_4 | GPIO_PIN_5 | GPIO_PIN_7;
    gpio.Mode = GPIO_MODE_INPUT;
    gpio.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &gpio);
    gpio.Pin = GPIO_PIN_6;
    gpio.Mode = GPIO_MODE_AF_PP;
    gpio.Speed = GPIO_SPEED_FREQ_HIGH;
    HAL_GPIO_Init(GPIOA, &gpio);

    hspi1.Instance = SPI1;
    hspi1.Init.Mode = SPI_MODE_SLAVE;
    hspi1.Init.Direction = SPI_DIRECTION_2LINES;
    hspi1.Init.DataSize = SPI_DATASIZE_8BIT;
    hspi1.Init.CLKPolarity = SPI_POLARITY_LOW;
    hspi1.Init.CLKPhase = SPI_PHASE_1EDGE;
    hspi1.Init.NSS = SPI_NSS_HARD_INPUT;
    hspi1.Init.FirstBit = SPI_FIRSTBIT_MSB;
    hspi1.Init.TIMode = SPI_TIMODE_DISABLE;
    hspi1.Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
    hspi1.Init.CRCPolynomial = 7;
    if (HAL_SPI_Init(&hspi1) != HAL_OK) Error_Handler();
    HAL_NVIC_SetPriority(SPI1_IRQn, 2, 0);
    HAL_NVIC_EnableIRQ(SPI1_IRQn);
}

static void UART1_Init(void) {
    __HAL_RCC_USART1_CLK_ENABLE();
    GPIO_InitTypeDef gpio = {0};
    gpio.Pin = GPIO_PIN_9;
    gpio.Mode = GPIO_MODE_AF_PP;
    gpio.Speed = GPIO_SPEED_FREQ_HIGH;
    HAL_GPIO_Init(GPIOA, &gpio);
    gpio.Pin = GPIO_PIN_10;
    gpio.Mode = GPIO_MODE_INPUT;
    gpio.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &gpio);

    huart1.Instance = USART1;
    huart1.Init.BaudRate = 115200;
    huart1.Init.WordLength = UART_WORDLENGTH_8B;
    huart1.Init.StopBits = UART_STOPBITS_1;
    huart1.Init.Parity = UART_PARITY_NONE;
    huart1.Init.Mode = UART_MODE_TX_RX;
    huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
    huart1.Init.OverSampling = UART_OVERSAMPLING_16;
    if (HAL_UART_Init(&huart1) != HAL_OK) Error_Handler();
}

static void Error_Handler(void) {
    __disable_irq();
    while (1) { }
}
