from fastapi import FastAPI
from fast_gaebabja_api.routes import krx, stock, exchange

app = FastAPI(title="FAST-GABABJA-API", version="1.0.0")

# 라우트 등록
app.include_router(krx.router, prefix="/krx", tags=["KRX Stocks"])
app.include_router(stock.router, prefix="/stock", tags=["Stock Price"])
app.include_router(exchange.router, prefix="/exchange", tags=["Exchange Rate"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FAST-GABABJA-API"}
