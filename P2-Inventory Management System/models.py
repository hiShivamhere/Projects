from pydantic import BaseModel, EmailStr
from typing import Optional

class Product(BaseModel):
    name: str
    description: Optional[str]
    price: float
    in_stock: bool = True

class User(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    email: EmailStr
    
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
