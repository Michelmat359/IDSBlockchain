"""Main script to run simulation experiments."""

from __future__ import annotations

import json
import random
import time
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from blockchain_logger import BlockchainLogger
from controller import PIDController, PIDParams
from data_generator import generate_batch
from evaluate_metrics import latency, throughput
from he_module import HEContext, HEModule
from ids_connector import IDSConnector, Policy
from sensitivity import SensitivityWeights, compute_sensitivity


def load_config() -> dict:
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


def main() -> None:
    cfg = load_config()
    weights = SensitivityWeights(**cfg["weights"])
    pid_params = PIDParams(**cfg["pid"])
    controller = PIDController(pid_params, initial=cfg["he"]["min_bits"])
    policy = Policy(min_bits=cfg["he"]["min_bits"])
    connector = IDSConnector(policy)
    logger = BlockchainLogger()

    stats = []
    start = time.time()
    current_time = 0
    while current_time < cfg["simulation"]["duration_minutes"] * 60:
        batch = generate_batch(64, 5)
        s = compute_sensitivity(
            random.random(), random.random(), random.random(), weights
        )
        target_bits = cfg["he"]["min_bits"] + s * (
            cfg["he"]["max_bits"] - cfg["he"]["min_bits"]
        )
        bits = int(controller.update(target_bits, controller.value, 1))
        bits = max(cfg["he"]["min_bits"], min(cfg["he"]["max_bits"], bits))
        allowed = connector.validate(bits)
        logger.log("policy_check", json.dumps({"bits": bits, "allowed": allowed}))

        he = HEModule(HEContext(bits))
        encode_times = []
        for val in batch.iloc[:, 0].values:
            t0 = time.time()
            enc = he.encrypt(float(val))
            he.decrypt(enc)
            encode_times.append(time.time() - t0)
        stats.append(
            {
                "time": current_time,
                "bits": bits,
                "latency": latency(encode_times),
            }
        )
        time.sleep(cfg["simulation"]["step_seconds"])
        current_time += cfg["simulation"]["step_seconds"]

    df = pd.DataFrame(stats)
    df.to_csv("results.csv", index=False)
    print("Average latency:", df["latency"].mean())
    print("Average bits:", df["bits"].mean())


if __name__ == "__main__":
    main()
