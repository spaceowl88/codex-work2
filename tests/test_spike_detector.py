from memehunter.logic.spike import SpikeDetector


def test_spike_detection():
    detector = SpikeDetector(window=3, thresh=1.0)
    assert not detector.update(1)
    assert not detector.update(1)
    assert detector.update(5)
