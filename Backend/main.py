from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.analyze import analyze as analyze_router

app = FastAPI(
    title="AI Fact Checking API",
    description="Vérification intelligente des sources et fact-checking",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "API Fact Checking active"}
