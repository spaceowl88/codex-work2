from __future__ import annotations

import json
from typing import Any


class DexChecker:
    """Parse pump.fun or pumpswap responses for coin information."""

    def __init__(self, data: dict[str, Any]):
        self.data = data

    @classmethod
    def from_json(cls, text: str) -> "DexChecker":
        return cls(json.loads(text))

    def coin_addresses(self) -> list[str]:
        """Return list of new coin mint addresses."""
        coins = self.data.get("coins", [])
        return [coin.get("address", "") for coin in coins]
