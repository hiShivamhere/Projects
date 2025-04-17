from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    description: Optional[str]
    price: float
    in_stock: bool = True
