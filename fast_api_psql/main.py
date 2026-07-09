from fastapi import FastAPI
from database import Base, engine
from routers import users

# Creates tables if they don't exist (use Alembic for real migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL running"}