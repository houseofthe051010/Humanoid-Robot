#pragma once

#include <stdbool.h>
#include <stdint.h>
#include "stm32f1xx_hal.h"

#define ODRIVE_COUNT 2U

typedef struct {
    float position_turns;
    float velocity_turns_s;
    uint32_t axis_error;
    uint8_t axis_state;
    uint32_t last_update_ms;
} ODriveFeedback;

void odrive_can_init(CAN_HandleTypeDef *can_handle);
bool odrive_set_position(uint8_t node_id, float position_turns,
                         float velocity_ff_turns_s, float torque_ff_nm);
bool odrive_enable_position_control(uint8_t node_id);
bool odrive_set_idle(uint8_t node_id);
bool odrive_clear_errors(uint8_t node_id);
bool odrive_estop_all(void);
void odrive_process_rx(const CAN_RxHeaderTypeDef *header, const uint8_t data[8]);
const ODriveFeedback *odrive_feedback(uint8_t node_id);

