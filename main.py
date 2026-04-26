from fastapi import FastAPI
from db.database import Base, engine
from routes import auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "JWT Auth Running"}

app.include_router(auth.router)