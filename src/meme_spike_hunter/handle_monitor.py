from __future__ import annotations


def tweet_mentions(
    text: str,
    author: str,
    *,
    handles: list[str],
    keywords: list[str],
) -> bool:
    """Return True if the tweet matches our monitoring criteria.

    Parameters
    ----------
    text : str
        Tweet text.
    author : str
        Tweet author handle.
    handles : list[str]
        List of handles to monitor.
    keywords : list[str]
        List of keywords to monitor.
    """
    if not any(h.lower() in author.lower() for h in handles):
        return False
    return any(k.lower() in text.lower() for k in keywords)
