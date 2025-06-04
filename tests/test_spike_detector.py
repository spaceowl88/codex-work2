from meme_spike_hunter.spike_detector import zscore_spike


def test_zscore_spike_positive():
    series = [1.0] * 15 + [10.0]
    assert zscore_spike(series)


def test_zscore_spike_negative():
    series = [1.0] * 16
    assert not zscore_spike(series)
