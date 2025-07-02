from fastapi import APIRouter, HTTPException, status, Depends
from fastapi_jwt_auth import AuthJWT
from schemas import UserLogin, UserRegister, TokenResponse
from database import SessionLocal, get_db
from models import User
from passlib.hash import bcrypt
from pydantic import constr
from typing import Dict, Any
from sqlalchemy.orm import Session

router = APIRouter()

# Minimum 8 chars, at least 1 uppercase, 1 lowercase, 1 number
PasswordStr = constr(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')

class UserRegisterWithValidation(UserRegister):
    password: PasswordStr

@router.post("/register", response_model=Dict[str, Any])
def register(
    user: UserRegisterWithValidation, 
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    existing_user = db.query(User).filter(User.username == user.username).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "registration_failed",
                "message": "Username already exists"
            }
        )

    hashed_password = bcrypt.hash(user.password)
    new_user = User(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "status": "success",
        "message": "User registered successfully",
        "user_id": new_user.id
    }

@router.post("/login", response_model=TokenResponse)
def login(
    user: UserLogin, 
    Authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db)
) -> Dict[str, str]:
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not bcrypt.verify(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "error": "authentication_failed",
                "message": "Invalid username or password"
            }
        )

    access_token = Authorize.create_access_token(subject=user.username)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
