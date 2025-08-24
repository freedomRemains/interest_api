from __future__ import annotations

from fastapi import FastAPI

from .api.routes import router as api_router
from .db.base import Base
from .db.session import engine

app = FastAPI(title="interest_api")

# Create tables for SQLite/dev automatically
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api")
