from fastapi import APIRouter, HTTPException
from fastapi_jwt_auth import AuthJWT
from schemas import UserLogin, TokenResponse
from database import SessionLocal
from models import User
from passlib.hash import bcrypt
from fastapi import Depends


router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    db = SessionLocal()
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not bcrypt.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = Authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}
