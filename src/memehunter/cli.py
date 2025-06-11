from __future__ import annotations

import asyncio
from collections import defaultdict
from typing import Any

import typer

from .collector.twitter import stream
from .logic.dex import check_new_pairs
from .logic.spike import SpikeDetector
from .notify.terminal import alert

app = typer.Typer()


@app.command()
def hunt(handles: str = "", keywords: str = "") -> None:
    """Monitor Twitter for spikes in keyword mentions."""
    handles_l = [h.strip() for h in handles.split(",") if h.strip()]
    keywords_l = [k.strip() for k in keywords.split(",") if k.strip()]

    q: asyncio.Queue[tuple[Any, Any]] = asyncio.Queue()
    detector = SpikeDetector()

    async def consumer() -> None:
        counts: defaultdict[str, int] = defaultdict(int)
        while True:
            ts, tweet = await q.get()
            for kw in keywords_l:
                if kw.lower() in tweet.text.lower():
                    counts[kw] += 1
            if ts.second % 15 == 0:
                for kw, c in counts.items():
                    if detector.update(c):
                        pairs = await check_new_pairs(kw)
                        alert(kw, c, pairs)
                counts.clear()

    asyncio.run(asyncio.gather(stream(keywords_l, handles_l, q), consumer()))


if __name__ == "__main__":
    app()
