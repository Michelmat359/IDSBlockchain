"""Simplified wrapper around homomorphic encryption operations."""

from dataclasses import dataclass

try:
    from Pyfhel import Pyfhel
except ImportError:  # pragma: no cover - optional dependency
    Pyfhel = None


@dataclass
class HEContext:
    bit_length: int


class HEModule:
    def __init__(self, context: HEContext):
        self.context = context
        if Pyfhel is not None:
            self.he = Pyfhel()
            self.he.contextGen(p=self.context.bit_length)
            self.he.keyGen()
        else:
            self.he = None

    def encrypt(self, value: float) -> float:
        if self.he:
            return self.he.encryptFrac(value)
        return value  # fallback: return plaintext

    def decrypt(self, value) -> float:
        if self.he:
            return self.he.decryptFrac(value)
        return float(value)
