#include "odrive_can.h"

#include <string.h>

enum {
    CAN_CMD_HEARTBEAT = 0x01,
    CAN_CMD_ESTOP = 0x02,
    CAN_CMD_SET_AXIS_STATE = 0x07,
    CAN_CMD_ENCODER_ESTIMATES = 0x09,
    CAN_CMD_SET_CONTROLLER_MODES = 0x0B,
    CAN_CMD_SET_INPUT_POSITION = 0x0C,
    CAN_CMD_CLEAR_ERRORS = 0x18,
};

enum {
    AXIS_STATE_IDLE = 1,
    AXIS_STATE_CLOSED_LOOP_CONTROL = 8,
    CONTROL_MODE_POSITION = 3,
    INPUT_MODE_PASSTHROUGH = 1,
};

static CAN_HandleTypeDef *odrive_can;
static ODriveFeedback feedback[ODRIVE_COUNT];

static uint32_t make_id(uint8_t node_id, uint8_t command_id) {
    return ((uint32_t)node_id << 5U) | command_id;
}

static bool send_frame(uint8_t node_id, uint8_t command_id,
                       const uint8_t *data, uint8_t length) {
    CAN_TxHeaderTypeDef header = {0};
    uint32_t mailbox;
    uint8_t payload[8] = {0};

    if (odrive_can == NULL || length > sizeof(payload)) {
        return false;
    }
    if (data != NULL && length != 0U) {
        memcpy(payload, data, length);
    }
    header.StdId = make_id(node_id, command_id);
    header.IDE = CAN_ID_STD;
    header.RTR = CAN_RTR_DATA;
    header.DLC = length;
    header.TransmitGlobalTime = DISABLE;
    return HAL_CAN_AddTxMessage(odrive_can, &header, payload, &mailbox) == HAL_OK;
}

static void put_u32_le(uint8_t *destination, uint32_t value) {
    destination[0] = (uint8_t)value;
    destination[1] = (uint8_t)(value >> 8U);
    destination[2] = (uint8_t)(value >> 16U);
    destination[3] = (uint8_t)(value >> 24U);
}

static uint32_t get_u32_le(const uint8_t *source) {
    return (uint32_t)source[0] | ((uint32_t)source[1] << 8U) |
           ((uint32_t)source[2] << 16U) | ((uint32_t)source[3] << 24U);
}

static void put_float_le(uint8_t *destination, float value) {
    uint32_t bits;
    memcpy(&bits, &value, sizeof(bits));
    put_u32_le(destination, bits);
}

static float get_float_le(const uint8_t *source) {
    uint32_t bits = get_u32_le(source);
    float value;
    memcpy(&value, &bits, sizeof(value));
    return value;
}

static int16_t scaled_i16(float value, float scale) {
    float scaled = value * scale;
    if (scaled > 32767.0f) scaled = 32767.0f;
    if (scaled < -32768.0f) scaled = -32768.0f;
    return (int16_t)scaled;
}

void odrive_can_init(CAN_HandleTypeDef *can_handle) {
    odrive_can = can_handle;
    memset(feedback, 0, sizeof(feedback));
}

bool odrive_set_position(uint8_t node_id, float position_turns,
                         float velocity_ff_turns_s, float torque_ff_nm) {
    uint8_t data[8];
    int16_t velocity = scaled_i16(velocity_ff_turns_s, 1000.0f);
    int16_t torque = scaled_i16(torque_ff_nm, 1000.0f);

    if (node_id >= ODRIVE_COUNT) return false;
    put_float_le(data, position_turns);
    data[4] = (uint8_t)velocity;
    data[5] = (uint8_t)((uint16_t)velocity >> 8U);
    data[6] = (uint8_t)torque;
    data[7] = (uint8_t)((uint16_t)torque >> 8U);
    return send_frame(node_id, CAN_CMD_SET_INPUT_POSITION, data, sizeof(data));
}

bool odrive_enable_position_control(uint8_t node_id) {
    uint8_t modes[8];
    uint8_t state[4];
    if (node_id >= ODRIVE_COUNT) return false;
    put_u32_le(modes, CONTROL_MODE_POSITION);
    put_u32_le(modes + 4, INPUT_MODE_PASSTHROUGH);
    put_u32_le(state, AXIS_STATE_CLOSED_LOOP_CONTROL);
    return send_frame(node_id, CAN_CMD_SET_CONTROLLER_MODES, modes, sizeof(modes)) &&
           send_frame(node_id, CAN_CMD_SET_AXIS_STATE, state, sizeof(state));
}

bool odrive_set_idle(uint8_t node_id) {
    uint8_t state[4];
    if (node_id >= ODRIVE_COUNT) return false;
    put_u32_le(state, AXIS_STATE_IDLE);
    return send_frame(node_id, CAN_CMD_SET_AXIS_STATE, state, sizeof(state));
}

bool odrive_clear_errors(uint8_t node_id) {
    return node_id < ODRIVE_COUNT && send_frame(node_id, CAN_CMD_CLEAR_ERRORS, NULL, 0);
}

bool odrive_estop_all(void) {
    bool success = true;
    for (uint8_t node = 0; node < ODRIVE_COUNT; ++node) {
        success = send_frame(node, CAN_CMD_ESTOP, NULL, 0) && success;
    }
    return success;
}

void odrive_process_rx(const CAN_RxHeaderTypeDef *header, const uint8_t data[8]) {
    if (header == NULL || header->IDE != CAN_ID_STD) return;
    uint8_t node = (uint8_t)(header->StdId >> 5U);
    uint8_t command = (uint8_t)(header->StdId & 0x1FU);
    if (node >= ODRIVE_COUNT) return;

    if (command == CAN_CMD_HEARTBEAT && header->DLC >= 5U) {
        feedback[node].axis_error = get_u32_le(data);
        feedback[node].axis_state = data[4];
        feedback[node].last_update_ms = HAL_GetTick();
    } else if (command == CAN_CMD_ENCODER_ESTIMATES && header->DLC == 8U) {
        feedback[node].position_turns = get_float_le(data);
        feedback[node].velocity_turns_s = get_float_le(data + 4);
        feedback[node].last_update_ms = HAL_GetTick();
    }
}

const ODriveFeedback *odrive_feedback(uint8_t node_id) {
    return node_id < ODRIVE_COUNT ? &feedback[node_id] : NULL;
}

