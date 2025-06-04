from __future__ import annotations

from typing import Any, List


async def check_new_pairs(keyword: str) -> List[dict[str, Any]]:
    """Return a dummy list of new pairs containing ``keyword``."""
    return [{"pair": f"SOL-{keyword.upper()}"}]
