from __future__ import annotations

from collections import deque
from statistics import mean, pstdev
from typing import Deque


class SpikeDetector:
    """Detect spikes in integer event counts using z-score."""

    def __init__(self, window: int = 60, thresh: float = 3.0) -> None:
        self.window = window
        self.thresh = thresh
        self._history: Deque[int] = deque(maxlen=window)

    def update(self, count: int) -> bool:
        """Add a new count and return ``True`` if it is a spike."""
        self._history.append(count)
        if len(self._history) < self.window:
            return False
        m = mean(self._history)
        stdev = pstdev(self._history)
        if stdev == 0:
            return False
        score = (self._history[-1] - m) / stdev
        return score >= self.thresh
