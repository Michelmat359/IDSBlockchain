"""Simplified IDS connector enforcing basic security policies."""

from dataclasses import dataclass


@dataclass
class Policy:
    min_bits: int = 128


class IDSConnector:
    def __init__(self, policy: Policy):
        self.policy = policy

    def validate(self, bit_length: int) -> bool:
        return bit_length >= self.policy.min_bits
