"""Simple CSV-based blockchain logger (simulated)."""

import csv
from pathlib import Path
from datetime import datetime


class BlockchainLogger:
    def __init__(self, path: str = "ledger.csv"):
        self.path = Path(path)
        if not self.path.exists():
            with self.path.open("w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "event", "detail"])

    def log(self, event: str, detail: str) -> None:
        with self.path.open("a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.utcnow().isoformat(), event, detail])
