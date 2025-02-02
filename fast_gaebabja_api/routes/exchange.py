from fastapi import APIRouter
from fast_gaebabja_api.services.exchange_service import get_exchange_rate

router = APIRouter()

@router.get("/rate/{currency}")
async def exchange_rate(currency: str):
    return {"currency": currency, "rate": get_exchange_rate(currency)}
