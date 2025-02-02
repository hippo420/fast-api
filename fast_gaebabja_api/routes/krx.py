from fastapi import APIRouter
from fast_gaebabja_api.services.krx_service import load_allstock_KRX

router = APIRouter()

@router.get("/stocks")
async def get_krx_stocks():
    return {"items": load_allstock_KRX()}
