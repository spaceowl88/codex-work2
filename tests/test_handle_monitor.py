from meme_spike_hunter.handle_monitor import tweet_mentions


def test_handle_and_keyword_match():
    assert tweet_mentions(
        "Check out this new coin!",
        "@elonmusk",
        handles=["crypto_whale", "elonmusk"],
        keywords=["coin"],
    )


def test_handle_not_monitored():
    assert not tweet_mentions(
        "Check out this new coin!",
        "@other",
        handles=["crypto_whale"],
        keywords=["coin"],
    )
