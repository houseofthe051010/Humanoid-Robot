"""Minimal Raspberry Pi SPI interface for the STM32 ankle controller."""

from dataclasses import dataclass
import struct
import time

import spidev


REQUEST = struct.Struct("<BBBBfff8x")
RESPONSE = struct.Struct("<BBBBffffI")


@dataclass
class Feedback:
    status: int
    last_command: int
    sequence: int
    position_turns: tuple[float, float]
    velocity_turns_s: tuple[float, float]
    combined_axis_error: int


class AnkleController:
    MOVE_POSITION = 1
    ENABLE = 2
    IDLE = 3
    ESTOP = 4
    CLEAR_ERRORS = 5

    def __init__(self, bus: int = 0, chip_select: int = 0, speed_hz: int = 500_000):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, chip_select)
        self.spi.max_speed_hz = speed_hz
        self.spi.mode = 0
        self.sequence = 0

    def close(self) -> None:
        self.spi.close()

    def _command(
        self,
        command: int,
        motor: int = 0,
        position_turns: float = 0.0,
        velocity_ff_turns_s: float = 0.0,
        torque_ff_nm: float = 0.0,
    ) -> Feedback:
        if motor not in (0, 1):
            raise ValueError("motor must be 0 or 1")
        self.sequence = (self.sequence + 1) & 0xFF
        request = REQUEST.pack(
            0xA5,
            command,
            motor,
            self.sequence,
            position_turns,
            velocity_ff_turns_s,
            torque_ff_nm,
        )
        self.spi.xfer2(list(request))

        # SPI is full-duplex, so the command result is returned by the next
        # transfer. Poll with NOP packets until the STM32 reports this sequence.
        nop = REQUEST.pack(0xA5, 0, motor, self.sequence, 0.0, 0.0, 0.0)
        values = None
        for _ in range(10):
            time.sleep(0.002)
            candidate = RESPONSE.unpack(bytes(self.spi.xfer2(list(nop))))
            if candidate[0] == 0x5A and candidate[2] == command and candidate[3] == self.sequence:
                values = candidate
                break
        if values is None:
            raise TimeoutError("STM32 did not acknowledge the SPI command")
        if values[0] != 0x5A:
            raise RuntimeError("invalid response from STM32")
        return Feedback(
            status=values[1],
            last_command=values[2],
            sequence=values[3],
            position_turns=(values[4], values[5]),
            velocity_turns_s=(values[6], values[7]),
            combined_axis_error=values[8],
        )

    def move_position(
        self,
        motor: int,
        position_turns: float,
        velocity_ff_turns_s: float = 0.0,
        torque_ff_nm: float = 0.0,
    ) -> Feedback:
        return self._command(
            self.MOVE_POSITION,
            motor,
            position_turns,
            velocity_ff_turns_s,
            torque_ff_nm,
        )

    def enable(self, motor: int) -> Feedback:
        return self._command(self.ENABLE, motor)

    def idle(self, motor: int) -> Feedback:
        return self._command(self.IDLE, motor)

    def clear_errors(self, motor: int) -> Feedback:
        return self._command(self.CLEAR_ERRORS, motor)

    def emergency_stop(self) -> Feedback:
        return self._command(self.ESTOP)
