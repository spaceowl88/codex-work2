from meme_spike_hunter.dex_checker import DexChecker

MOCK_RESPONSE = {
    "coins": [
        {"address": "Mint1"},
        {"address": "Mint2"},
    ]
}


def test_coin_addresses_parsing():
    checker = DexChecker(MOCK_RESPONSE)
    assert checker.coin_addresses() == ["Mint1", "Mint2"]
