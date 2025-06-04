import asyncio
from types import SimpleNamespace

import pytest

from memehunter.collector.twitter import stream


class DummyStream:
    instances: list["DummyStream"] = []

    def __init__(self, token: str, queue: asyncio.Queue):
        self.queue = queue
        self.added_rules: list[str] = []
        DummyStream.instances.append(self)

    async def add_rules(self, rules, **kwargs):
        self.added_rules.extend(r.value for r in rules)

    async def filter(self, *args, **kwargs):
        tweet = SimpleNamespace(text="hello", created_at=None)
        await self.queue.put((asyncio.get_event_loop().time(), tweet))


@pytest.mark.asyncio
async def test_stream_adds_handle_rules(monkeypatch):
    q: asyncio.Queue = asyncio.Queue()
    monkeypatch.setattr("memehunter.collector.twitter._QueueStream", DummyStream)
    await stream([], ["elonmusk"], q)
    assert DummyStream.instances
    assert "from:elonmusk" in DummyStream.instances[-1].added_rules
