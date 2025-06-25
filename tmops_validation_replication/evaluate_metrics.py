"""Utility functions for evaluating metrics."""

import numpy as np


def throughput(processed: int, duration: float) -> float:
    return processed / duration if duration > 0 else 0.0


def latency(times: list[float]) -> float:
    return float(np.mean(times)) if times else 0.0
