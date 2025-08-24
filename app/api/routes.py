from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db.crud import (
    create_interest,
    get_interests_with_items,
    logical_delete_interest,
    update_interest,
)
from ..db.models import Interest
from ..db.session import SessionLocal
from .schemas import InterestCreate, InterestOut, InterestUpdate

router = APIRouter()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/interests", response_model=List[InterestOut])
def get_interest_map(db: Session = Depends(get_db)) -> List[InterestOut]:
    # 関心事と紐づくアイテムのマップ取得（削除済みは含めない）
    interests: List[Interest] = get_interests_with_items(db)
    result = []
    for it in interests:
        it_dict = {
            "INTEREST_ID": it.interest_id,
            "TITLE": it.title,
            "VERSION": it.version,
            "IS_DELETED": it.is_deleted,
            "CREATED_BY": it.created_by,
            "CREATED_AT": it.created_at,
            "UPDATED_BY": it.updated_by,
            "UPDATED_AT": it.updated_at,
            "items": [
                {
                    "ITEM_ID": i.item_id,
                    "ARTICLE": i.article,
                    "LINK": i.link,
                    "FILE_PATH": i.file_path,
                    "INTEREST_ID": i.interest_id,
                    "VERSION": i.version,
                    "IS_DELETED": i.is_deleted,
                    "CREATED_BY": i.created_by,
                    "CREATED_AT": i.created_at,
                    "UPDATED_BY": i.updated_by,
                    "UPDATED_AT": i.updated_at,
                }
                for i in it.items
            ],
        }
        result.append(InterestOut.model_validate(it_dict))
    return result


@router.post("/interests", response_model=InterestOut, status_code=status.HTTP_201_CREATED)
def create_interest_endpoint(payload: InterestCreate, db: Session = Depends(get_db)) -> InterestOut:
    new_interest = create_interest(db, title=payload.title, created_by=payload.created_by)
    it_dict = {
        "INTEREST_ID": new_interest.interest_id,
        "TITLE": new_interest.title,
        "VERSION": new_interest.version,
        "IS_DELETED": new_interest.is_deleted,
        "CREATED_BY": new_interest.created_by,
        "CREATED_AT": new_interest.created_at,
        "UPDATED_BY": new_interest.updated_by,
        "UPDATED_AT": new_interest.updated_at,
        "items": [],
    }
    return InterestOut.model_validate(it_dict)


@router.put("/interests/{interest_id}", response_model=InterestOut)
def update_interest_endpoint(
    interest_id: int, payload: InterestUpdate, db: Session = Depends(get_db)
) -> InterestOut:
    updated = update_interest(
        db, interest_id=interest_id, title=payload.title, updated_by=payload.updated_by
    )
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interest not found")
    it_dict = {
        "INTEREST_ID": updated.interest_id,
        "TITLE": updated.title,
        "VERSION": updated.version,
        "IS_DELETED": updated.is_deleted,
        "CREATED_BY": updated.created_by,
        "CREATED_AT": updated.created_at,
        "UPDATED_BY": updated.updated_by,
        "UPDATED_AT": updated.updated_at,
        "items": [
            {
                "ITEM_ID": i.item_id,
                "ARTICLE": i.article,
                "LINK": i.link,
                "FILE_PATH": i.file_path,
                "INTEREST_ID": i.interest_id,
                "VERSION": i.version,
                "IS_DELETED": i.is_deleted,
                "CREATED_BY": i.created_by,
                "CREATED_AT": i.created_at,
                "UPDATED_BY": i.updated_by,
                "UPDATED_AT": i.updated_at,
            }
            for i in updated.items
        ],
    }
    return InterestOut.model_validate(it_dict)


@router.delete("/interests/{interest_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_interest_endpoint(interest_id: int, db: Session = Depends(get_db)) -> None:
    ok = logical_delete_interest(db, interest_id=interest_id, updated_by="system")
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interest not found")
    return None
