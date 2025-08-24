from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Interest(Base):
    __tablename__ = "INTEREST"

    interest_id: Mapped[int] = mapped_column(
        "INTEREST_ID", Integer, primary_key=True, autoincrement=True
    )
    title: Mapped[Optional[str]] = mapped_column("TITLE", String(256))
    version: Mapped[Optional[int]] = mapped_column("VERSION", Integer, default=1)
    is_deleted: Mapped[int] = mapped_column("IS_DELETED", Integer, default=0)
    created_by: Mapped[Optional[str]] = mapped_column("CREATED_BY", String(128))
    created_at: Mapped[Optional[datetime]] = mapped_column("CREATED_AT", DateTime)
    updated_by: Mapped[Optional[str]] = mapped_column("UPDATED_BY", String(128))
    updated_at: Mapped[Optional[datetime]] = mapped_column("UPDATED_AT", DateTime)

    items: Mapped[List["Item"]] = relationship(
        "Item",
        back_populates="interest",
        primaryjoin="and_(Interest.interest_id==Item.interest_id, Item.is_deleted==0)",
        lazy="selectin",
    )


class Item(Base):
    __tablename__ = "ITEM"

    item_id: Mapped[int] = mapped_column("ITEM_ID", Integer, primary_key=True, autoincrement=True)
    article: Mapped[Optional[str]] = mapped_column("ARTICLE", Text)
    link: Mapped[Optional[str]] = mapped_column("LINK", String(1024))
    file_path: Mapped[Optional[str]] = mapped_column("FILE_PATH", String(1024))
    interest_id: Mapped[Optional[int]] = mapped_column(
        "INTEREST_ID", ForeignKey("INTEREST.INTEREST_ID")
    )
    version: Mapped[Optional[int]] = mapped_column("VERSION", Integer, default=1)
    is_deleted: Mapped[int] = mapped_column("IS_DELETED", Integer, default=0)
    created_by: Mapped[Optional[str]] = mapped_column("CREATED_BY", String(128))
    created_at: Mapped[Optional[datetime]] = mapped_column("CREATED_AT", DateTime)
    updated_by: Mapped[Optional[str]] = mapped_column("UPDATED_BY", String(128))
    updated_at: Mapped[Optional[datetime]] = mapped_column("UPDATED_AT", DateTime)

    interest: Mapped["Interest"] = relationship("Interest", back_populates="items")
