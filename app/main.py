from fastapi import FastAPI
from app.routes.users import router as users_router

app = FastAPI(
    title="x402 API",
    description="Professional REST API built with FastAPI",
    version="1.0.0"
)

app.include_router(users_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to x402 API",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
