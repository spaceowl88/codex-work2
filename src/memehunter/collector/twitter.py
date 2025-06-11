from __future__ import annotations

import asyncio
import os
from datetime import datetime, timezone
from typing import List

import tweepy
from tweepy.asynchronous import AsyncStreamingClient


class _QueueStream(AsyncStreamingClient):
    """Streaming client that puts received tweets into an asyncio queue."""

    def __init__(self, bearer_token: str, queue: asyncio.Queue):
        super().__init__(bearer_token)
        self.queue = queue

    async def on_tweet(self, tweet: tweepy.Tweet) -> None:  # type: ignore[type-arg]
        await self.queue.put((datetime.now(timezone.utc), tweet))


async def stream(keywords: List[str], handles: List[str], queue: asyncio.Queue) -> None:
    """Start a Tweepy filtered stream and push tweets into ``queue``.

    Parameters
    ----------
    keywords : list[str]
        Keywords to monitor.
    handles : list[str]
        Twitter handles to monitor.
    queue : asyncio.Queue
        Destination queue for received tweets.
    """
    token = os.getenv("TWITTER_BEARER_TOKEN", "")
    client = _QueueStream(token, queue)

    rules: List[tweepy.StreamRule] = []
    rules.extend(tweepy.StreamRule(f"{kw} lang:en") for kw in keywords)
    rules.extend(tweepy.StreamRule(f"from:{handle.lstrip('@')}") for handle in handles)

    if rules:
        await client.add_rules(rules, dry_run=True)

    await client.filter(tweet_fields=["created_at"])
 