from __future__ import annotations

import os
import tempfile

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base import Base
from app.main import app


@pytest.fixture(scope="function", autouse=True)
def setup_sqlite_tmp(monkeypatch):
    db_fd, db_path = tempfile.mkstemp(suffix=".db")
    os.close(db_fd)
    test_db_url = f"sqlite:///{db_path}"
    engine = create_engine(test_db_url, connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # swap SessionLocal used in routes
    monkeypatch.setattr("app.api.routes.SessionLocal", TestingSessionLocal)

    yield

    try:
        os.remove(db_path)
    except FileNotFoundError:
        pass


def test_interest_crud_flow():
    client = TestClient(app)

    res = client.get("/api/interests")
    assert res.status_code == 200
    assert res.json() == []

    res = client.post("/api/interests", json={"title": "Test interest", "created_by": "tester"})
    assert res.status_code == 201
    body = res.json()
    assert body["TITLE"] == "Test interest"
    interest_id = body["INTEREST_ID"]

    res = client.get("/api/interests")
    assert res.status_code == 200
    data = res.json()
    assert len(data) == 1
    assert data[0]["INTEREST_ID"] == interest_id

    res = client.put(
        f"/api/interests/{interest_id}", json={"title": "Updated", "updated_by": "tester2"}
    )
    assert res.status_code == 200
    assert res.json()["TITLE"] == "Updated"

    res = client.delete(f"/api/interests/{interest_id}")
    assert res.status_code == 204

    res = client.get("/api/interests")
    assert res.status_code == 200
    assert res.json() == []
