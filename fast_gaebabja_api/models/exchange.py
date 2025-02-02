from pydantic import BaseModel

class ExchangeRate(BaseModel):
    currency: str
    rate: float
