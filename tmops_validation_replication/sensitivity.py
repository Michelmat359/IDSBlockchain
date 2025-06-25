from dataclasses import dataclass


@dataclass
class SensitivityWeights:
    legal: float
    business: float
    privacy: float


def compute_sensitivity(c_legal: float, c_business: float, c_privacy: float, weights: SensitivityWeights) -> float:
    """Compute sensitivity as weighted sum of concerns."""
    return (
        weights.legal * c_legal
        + weights.business * c_business
        + weights.privacy * c_privacy
    )
