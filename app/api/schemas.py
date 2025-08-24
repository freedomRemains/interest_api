from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class ItemOut(BaseModel):
    item_id: int = Field(alias="ITEM_ID")
    article: Optional[str] = Field(None, alias="ARTICLE")
    link: Optional[str] = Field(None, alias="LINK")
    file_path: Optional[str] = Field(None, alias="FILE_PATH")
    interest_id: Optional[int] = Field(None, alias="INTEREST_ID")
    version: Optional[int] = Field(None, alias="VERSION")
    is_deleted: int = Field(alias="IS_DELETED")
    created_by: Optional[str] = Field(None, alias="CREATED_BY")
    created_at: Optional[datetime] = Field(None, alias="CREATED_AT")
    updated_by: Optional[str] = Field(None, alias="UPDATED_BY")
    updated_at: Optional[datetime] = Field(None, alias="UPDATED_AT")

    class Config:
        populate_by_name = True


class InterestOut(BaseModel):
    interest_id: int = Field(alias="INTEREST_ID")
    title: Optional[str] = Field(None, alias="TITLE")
    version: Optional[int] = Field(None, alias="VERSION")
    is_deleted: int = Field(alias="IS_DELETED")
    created_by: Optional[str] = Field(None, alias="CREATED_BY")
    created_at: Optional[datetime] = Field(None, alias="CREATED_AT")
    updated_by: Optional[str] = Field(None, alias="UPDATED_BY")
    updated_at: Optional[datetime] = Field(None, alias="UPDATED_AT")
    items: List[ItemOut] = []

    class Config:
        populate_by_name = True


class InterestCreate(BaseModel):
    title: str
    created_by: Optional[str] = None


class InterestUpdate(BaseModel):
    title: Optional[str] = None
    updated_by: Optional[str] = None
