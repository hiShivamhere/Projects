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
    role : str = "viewer"  # Default role is 'viewer'

class UserOut(BaseModel):
    email: EmailStr
    role : str
    
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
