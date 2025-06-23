import numpy as np
import pandas as pd


def generate_batch(size: int = 100, num_features: int = 10) -> pd.DataFrame:
    """Generate a synthetic batch of data."""
    X = np.random.randn(size, num_features)
    y = np.random.randint(0, 2, size)
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(num_features)])
    df["target"] = y
    return df
