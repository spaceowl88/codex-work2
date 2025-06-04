from __future__ import annotations

from collections import deque
from typing import Iterable


def zscore_spike(
    series: Iterable[float],
    *,
    window: int = 15,
    threshold: float = 3.0,
) -> bool:
    """Return True if the latest value is a positive spike.

    Parameters
    ----------
    series : Iterable[float]
        Time series values ordered from oldest to newest.
    window : int, default 15
        Moving window size.
    threshold : float, default 3.0
        Z-score threshold for spike detection.
    """
    data = list(series)
    if len(data) < window + 1:
        raise ValueError("series must contain at least window + 1 points")

    history = deque(data[-(window + 1) : -1], maxlen=window)
    latest = data[-1]
    mean = sum(history) / window
    variance = sum((x - mean) ** 2 for x in history) / window
    std = variance**0.5
    if std == 0:
        return latest > mean
    score = (latest - mean) / std
    return score >= threshold
