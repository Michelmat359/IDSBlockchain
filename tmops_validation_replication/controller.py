from dataclasses import dataclass


@dataclass
class PIDParams:
    kp: float
    ki: float
    kd: float


class PIDController:
    def __init__(self, params: PIDParams, initial: float = 0.0):
        self.params = params
        self.integral = 0.0
        self.prev_error = 0.0
        self.value = initial

    def update(self, target: float, measurement: float, dt: float) -> float:
        error = target - measurement
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0
        self.prev_error = error
        self.value += (
            self.params.kp * error
            + self.params.ki * self.integral
            + self.params.kd * derivative
        )
        return self.value
