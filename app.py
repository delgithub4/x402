from fastapi import FastAPI

app = FastAPI(
    title="x402 API",
    description="A modern REST API built with FastAPI.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to x402 API",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
