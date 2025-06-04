# Meme-Coin Spike Hunter

CLI/웹 하이브리드 툴로, Twitter(X) 트렌드와 DEX 활동을 실시간으로 모니터링하여 밈코인의 급등 조짐을 탐지합니다.

```
 Twitter  ---> Spike detector --+--> Alarm
 Handles --^
 Dex API  ---------------------'
```

## Quickstart

```bash
# 의존성 설치
poetry install

# 테스트 실행
poetry run pytest

# 예시: 특정 핸들 모니터링
poetry run python -m meme_spike_hunter.cli --handles crypto_whale,elonmusk --keywords doge
```

## 비용 추정

| 서비스                | 요금제                         | 월 예상 비용 |
|-----------------------|--------------------------------|-------------|
| QuickNode Solana RPC  | Free Tier (10 M credits)        | $0          |
| Twitter API           | Essential + Apify Trends Backup | $0          |
| 기타(서버 등)         | -                              | 사용량에 따라 |

## 라이선스

MIT
