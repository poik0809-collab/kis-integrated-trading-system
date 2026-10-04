# kis-integrated-trading-system

한국투자증권 자동매매 통합 시스템 - Auto Trading System, Huntety Bot, pykis, mojito2, kis-auto-trader 베스트 프랙티스 조합

이 저장소는 한국투자증권 Open API를 기반으로 한 자동매매 시스템을 통합적으로 구성하기 위한 실전형 프로젝트 구조를 정리한 문서입니다. 여러 공개 오픈소스 구현과 실전 패턴을 참고하여, 실제 거래 시스템에서 자주 필요한 기능들을 모듈 단위로 정리했습니다.

## 프로젝트 소개

한국투자증권의 API를 활용한 자동매매 시스템은 보통 다음과 같은 단계로 구성됩니다.

- 계정 인증 및 토큰 발급
- 시세/호가/체결 데이터 수집
- 조건 검색 기반 신호 생성
- 주문 전송 및 체결 추적
- 잔고 및 포지션 관리
- 손절/익절 및 리스크 제어
- 로그 기록 및 운영 모니터링

이 저장소는 이를 안정적으로 운영하기 위해 필요한 기본 구조를 제공하며, 기술 검증, 모의투자 테스트, 실제 매매 환경 전환까지 고려한 설계에 초점을 둡니다.

## 주요 기능

- 한국투자증권 Open API 연동
- 인증 및 토큰 갱신 관리
- 실시간 시세 수집
- 주식/ETF/상품별 주문 처리
- 포트폴리오와 리스크 관리
- 로그와 상태 모니터링
- 전략 엔진 기반 확장 구조
- 모의투자와 실전 환경 분리

## 디렉터리 구조

```text
kis-integrated-trading-system/
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── kis_client.py
│   │   └── websocket_client.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   └── scheduler.py
│   ├── data/
│   │   ├── collector.py
│   │   ├── database.py
│   │   └── models.py
│   ├── order/
│   │   ├── execution.py
│   │   └── order_manager.py
│   ├── risk/
│   │   ├── position_manager.py
│   │   └── risk_manager.py
│   ├── strategies/
│   │   ├── base_strategy.py
│   │   ├── breakout.py
│   │   └── momentum.py
│   └── utils/
│       ├── notifications.py
│       ├── signal_utils.py
│       └── time_utils.py
├── backtest/
│   ├── engine.py
│   ├── metrics.py
│   └── dataset.py
├── tests/
│   ├── test_auth.py
│   ├── test_order.py
│   └── test_strategy.py
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## 기술 스택

- Python 3.10+
- requests / httpx
- pandas / numpy
- SQLAlchemy
- APScheduler
- python-dotenv
- SQLite 또는 PostgreSQL
- WebSocket 기반 실시간 데이터 수집

## 설치 방법

```bash
git clone https://github.com/poik0809-collab/kis-integrated-trading-system.git
cd kis-integrated-trading-system
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# Windows
# .venv\Scripts\activate
pip install -r requirements.txt
```

## 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 아래 항목을 입력합니다.

```env
KIS_APP_KEY=your_app_key
KIS_APP_SECRET=your_app_secret
KIS_ACCOUNT_NO=your_account_no
KIS_CANO=your_cano
KIS_ACNT_PRDT_CD=your_acnt_prdt_cd
KIS_MODE=MOCK
KIS_BASE_URL=https://openapi.koreainvestment.com:9443
```

> `KIS_MODE`는 `REAL` 또는 `MOCK` 중 하나로 설정할 수 있습니다.

## 실행 예시

### 모의투자 연결 테스트

```bash
python -m app.api.kis_client
```

### 백테스트 실행

```bash
python -m backtest.engine
```

### 자동매매 실행

```bash
python -m app.core.scheduler
```

## 사용 흐름

1. API 인증 및 토큰 발급
2. 계좌/잔고 확인
3. 시장 데이터 수집
4. 전략 신호 생성
5. 조건 충족 시 주문 전송
6. 체결 결과 기록 및 보관
7. 로그와 모니터링 반영

## 보안 주의사항

- API 키와 시크릿은 절대 공개 저장소에 업로드하지 마세요.
- `.env` 파일은 `.gitignore`에 포함하여 관리하세요.
- 모의투자 환경에서 충분히 검증한 뒤 실제 계좌에 적용하세요.
- 실제 거래는 위험이 존재하므로, 손절/익절/리스크 제한 로직을 반드시 구현하세요.

## 주의사항

이 프로젝트는 교육 및 개발 실험 목적을 포함한 자동매매 구조를 정리한 저장소입니다. 투자 결정을 최종적으로 책임지는 것은 사용자가며, 모든 거래에는 손실 가능성이 있습니다.

실전 운영 전에 반드시 
- 한국투자증권 Open API 문서 확인
- 모의투자 기반 검증
- 계좌 정책과 보안 가이드 준수
를 확인하시기 바랍니다.

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 참고 자료

- 한국투자증권 Open API 개발자센터: https://apiportal.koreainvestment.com/
- Auto Trading System: https://github.com/tawbury/Auto_Trading_System
- Auto-stock-trading-bot: https://github.com/Huntety/Auto-stock-trading-bot
- pykis: https://github.com/yhjoo/pykis
- kis-auto-trader: https://github.com/parkminyong/kis-auto-trader
