from enum import Enum

from fastapi import Query
from pydantic import BaseModel, Field, validator
from beanie import Document


class NotificationKeyEnum(str, Enum):
    registration = "registration"
    new_message = "new_message"
    new_post = "new_post"
    new_login = "new_login"


class Notification(BaseModel):
    user_id: str = Field(..., min_length=24, max_length=24)
    target_id: str | None = Field(None, min_length=24, max_length=24)
    key: NotificationKeyEnum
    data: dict | None = {}

    @validator('data', pre=True, always=True)
    def set_default_data(cls, v):
        return {} or v


class ListNotificationParams(BaseModel):
    user_id: str
    skip: int = Query(0, ge=0)
    limit: int = Query(10, ge=1)


class ReadNotificationParams(BaseModel):
    user_id: str
    notification_id: str
