"""Main script to run simulation experiments."""

from __future__ import annotations

import json
import random
import time
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
import matplotlib.pyplot as plt


from blockchain_logger import BlockchainLogger
from controller import PIDController, PIDParams
from data_generator import generate_batch
from evaluate_metrics import latency, throughput
from he_module import HEContext, HEModule
from ids_connector import IDSConnector, Policy
from sensitivity import SensitivityWeights, compute_sensitivity
from ml_pipeline import train_xgboost



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

        total_time = sum(encode_times)
        thpt = throughput(len(encode_times), total_time)

        noise = (cfg["he"]["max_bits"] - bits) / cfg["he"]["max_bits"] * 0.1
        noisy = batch.iloc[:, :-1].values + np.random.normal(
            0, noise, size=(len(batch), batch.shape[1] - 1)
        )
        labels = batch["target"].values
        model = train_xgboost(noisy, labels)
        preds = model.predict(noisy)
        acc = (preds == labels).mean()

        stats.append(
            {
                "time": current_time,
                "bits": bits,
                "sensitivity": s,
                "latency": latency(encode_times),
                "throughput": thpt,
                "accuracy": acc,

            }
        )
        time.sleep(cfg["simulation"]["step_seconds"])
        current_time += cfg["simulation"]["step_seconds"]

    df = pd.DataFrame(stats)
    df.to_csv("results.csv", index=False)
    print("Average latency:", df["latency"].mean())
    print("Average bits:", df["bits"].mean())

    plt.figure()
    plt.plot(df["sensitivity"], df["bits"], marker="o")
    plt.xlabel("Sensitivity")
    plt.ylabel("Bit length")
    plt.title("Adaptation of encryption parameters to data sensitivity")
    plt.tight_layout()
    plt.savefig("plot_sensitivity_bits.png")

    plt.figure()
    plt.scatter(df["bits"], df["latency"], c="tab:red")
    plt.xlabel("Bit length")
    plt.ylabel("Latency (s)")
    plt.title("Trade-off between efficiency and security")
    plt.tight_layout()
    plt.savefig("plot_latency_bits.png")

    plt.figure()
    plt.plot(df["bits"], df["accuracy"], marker="x", color="tab:green")
    plt.xlabel("Bit length")
    plt.ylabel("Accuracy")
    plt.title("Model accuracy under different encryption precision")
    plt.tight_layout()
    plt.savefig("plot_accuracy_bits.png")


if __name__ == "__main__":
    main()
