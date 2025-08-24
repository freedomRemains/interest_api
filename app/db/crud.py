from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Interest, Item


def get_interests_with_items(db: Session) -> List[Interest]:
    stmt = select(Interest).where(Interest.is_deleted == 0)
    interests = list(db.scalars(stmt))
    for it in interests:
        _ = it.items
    return interests


def create_interest(db: Session, title: str, created_by: Optional[str] = None) -> Interest:
    interest = Interest(
        title=title,
        version=1,
        is_deleted=0,
        created_by=created_by,
        created_at=datetime.now(),
        updated_by=created_by,
        updated_at=datetime.now(),
    )
    db.add(interest)
    db.flush()
    return interest


def update_interest(
    db: Session, interest_id: int, title: Optional[str], updated_by: Optional[str]
) -> Optional[Interest]:
    stmt = select(Interest).where(Interest.interest_id == interest_id, Interest.is_deleted == 0)
    interest = db.scalar(stmt)
    if not interest:
        return None
    if title is not None:
        interest.title = title
    interest.version = (interest.version or 0) + 1
    interest.updated_by = updated_by
    interest.updated_at = datetime.now()
    db.flush()
    return interest


def logical_delete_interest(db: Session, interest_id: int, updated_by: Optional[str]) -> bool:
    stmt = select(Interest).where(Interest.interest_id == interest_id, Interest.is_deleted == 0)
    interest = db.scalar(stmt)
    if not interest:
        return False

    interest.is_deleted = 1
    interest.updated_by = updated_by
    interest.updated_at = datetime.now()

    items_stmt = select(Item).where(Item.interest_id == interest_id, Item.is_deleted == 0)
    for item in db.scalars(items_stmt):
        item.is_deleted = 1
        item.updated_by = updated_by
        item.updated_at = datetime.now()

    db.flush()
    return True
