from sqlalchemy.orm import Session
from db import models
from core.security import hash_password, verify_password

def create_user(db: Session, email: str, password: str):
    existing = db.query(models.User).filter(models.User.email == email).first()
    if existing:
        return None

    user = models.User(email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user