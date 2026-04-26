from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from schemas.user import UserCreate, Token
from services.auth_service import create_user, authenticate_user
from db.database import get_db
from core.security import create_access_token
from core.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])


# ✅ REGISTER
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user.email, user.password)

    if not new_user:
        raise HTTPException(status_code=400, detail="User already exists")

    return {"message": "User created successfully"}


# ✅ LOGIN (OAuth2 compatible)
@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = authenticate_user(db, form_data.username, form_data.password)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# 🔒 PROTECTED ROUTE
@router.get("/profile")
def get_profile(current_user = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email
    }