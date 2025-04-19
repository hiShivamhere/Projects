from fastapi import APIRouter, HTTPException
from models import User, UserOut, Token
from auth import hash_password, verify_password, create_access_token
from datetime import timedelta
from database import db

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(user: User):
    if await db["users"].find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = hash_password(user.password)
    await db["users"].insert_one({"email": user.email, "password": hashed})
    return {"email": user.email}

@router.post("/login", response_model=Token)
async def login(user: User):
    db_user = await db["users"].find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}
