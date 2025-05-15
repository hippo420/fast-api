# Financial API

이 프로젝트는 KRX 주식 데이터, 주가 조회, 환율 데이터를 제공하는 FastAPI 기반 REST API입니다.

## 🚀 실행 방법

### 1️⃣ 로컬 실행
```sh
pip install -r requirements.txt
uvicorn fast_gaebabja_api.main:app --host 0.0.0.0 --port 3100
```

### 2️⃣ Docker 실행
```sh
docker build -t fast-gaebabja-api .
docker run -d -p 3100:3100 --name fast-gaebabja-api-container fast-gaebabja-api
```

### 3️⃣ API 테스트
```sh
curl http://localhost:3100/krx/stocks
curl http://localhost:3100/stock/price/005930
curl http://localhost:3100/exchange/rate/USD
```

## **✅ 정리**
이제 `fast-gaebabja-api` 패키지는:
- KRX 종목 정보 조회 (`/krx/stocks`)
- 주식 가격 조회 (`/stock/price/{code}`)
- 환율 정보 조회 (`/exchange/rate/{currency}`)
- Docker로 배포 가능

이제 바로 실행해보세요! 🚀
