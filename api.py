from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Загружаем переменные окружения
load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to RSPT API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
