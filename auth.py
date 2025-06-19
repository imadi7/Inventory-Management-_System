from fastapi import APIRouter, HTTPException, status, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from schemas import UserLogin, UserRegister, TokenResponse
from database import SessionLocal
from models import User
from passlib.hash import bcrypt

router = APIRouter()

@router.post("/register")
def register(user: UserRegister):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.username == user.username).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    hashed_password = bcrypt.hash(user.password)
    new_user = User(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    db = SessionLocal()
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not bcrypt.verify(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = Authorize.create_access_token(subject=user.username)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
