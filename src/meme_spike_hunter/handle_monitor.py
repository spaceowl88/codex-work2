from __future__ import annotations

from typing import Sequence


def tweet_mentions(
    tweet_text: str,
    tweet_handle: str,
    *,
    handles: Sequence[str],
    keywords: Sequence[str],
) -> bool:
    """Return True if the tweet is from a monitored handle and mentions keywords."""
    handle_normalized = tweet_handle.lstrip("@").lower()
    if handle_normalized not in {h.lstrip("@").lower() for h in handles}:
        return False

    text_lower = tweet_text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)
