from __future__ import annotations

from typing import Any, List

from rich.console import Console


def alert(keyword: str, count: int, pairs: List[dict[str, Any]]) -> None:
    """Display a colored alert about a detected spike."""
    console = Console()
    if pairs:
        console.print(f"[bold green]{keyword}[/] spike ({count}) - new pairs: {pairs}")
    else:
        console.print(
            f"[bold yellow]{keyword}[/] spike ({count}) - \N{ALARM CLOCK} Spike만 감지, 신규 Pair 없음"
        )
