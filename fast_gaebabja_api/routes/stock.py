from fastapi import APIRouter
from fast_gaebabja_api.services.stock_service import get_stock_price

router = APIRouter()

@router.get("/price/{code}")
async def stock_price(code: str):
    return {"code": code, "price": get_stock_price(code)}
