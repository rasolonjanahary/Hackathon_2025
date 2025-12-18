import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./data.db"
)

GOOGLE_FACT_CHECK_API_KEY = os.getenv("GOOGLE_FACT_CHECK_API_KEY", "")
