from __future__ import annotations

from typing import Any, List


class DexChecker:
    """Check for new DEX pairs."""

    def __init__(self, response: dict[str, Any]) -> None:
        """Initialize with a DEX API response."""
        self.response = response

    def coin_addresses(self) -> List[str]:
        """Return a list of coin addresses from the response."""
        return [coin["address"] for coin in self.response["coins"]]
