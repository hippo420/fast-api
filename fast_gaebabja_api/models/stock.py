from pydantic import BaseModel

class Stock(BaseModel):
    code: str
    price: float