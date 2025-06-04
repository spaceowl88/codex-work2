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

## 개발 타임라인

| 주차 | 목표 | 산출물 |
|------|------|--------|
| W0 | 🟢 **Kick-off** – 위 초기 파일 세트 생성 & 첫 커밋 | v0.0.1 |
| W1 | Twitter 수집기 완성, 키워드/핸들 필터 동작 확인 | `twitter.py` |
| W2 | Spike Detector 로직 + 단위 테스트 강화 | `spike.py` |
| W3 | Dex 모니터링(pump.fun/pumpswap/dexscreener) 통합 | `dex.py` |
| W4 | Typer CLI: `hunt`, `add-handle`, 알림(터미널·시스템) 연결 | `cli.py` |
| W5 | 로깅·리트라이·Docker, 비용 최적화 메모 | v0.1.0 |

## 라이선스

MIT

## 다음 할 일 (To-Do)

- Twitter 수집기 구현
- Spike Detector 테스트 보강
- DEX 모니터링 통합
