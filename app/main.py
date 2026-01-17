from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import student
from app.database import engine
from app import models

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",   # your HTML frontend
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(student.router)
