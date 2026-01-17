from fastapi import FastAPI
from database import engine
from app import models

models.Base.create_all(bind=engine)
