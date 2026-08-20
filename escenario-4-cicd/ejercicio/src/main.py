from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def index():
    return {
        "mensaje": "Hola desde Docker + CI/CD (ejercicio)!",
        "version": "1.0.0",
        "entorno": os.environ.get("ENV", "development")
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
