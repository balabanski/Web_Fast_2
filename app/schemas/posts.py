from datetime import datetime
from pydantic import BaseModel


class PostModel(BaseModel):
    """Проверить данные запроса"""
    title: str
    content: str


class PostDetailsModel(PostModel):
    """Вернуть данные ответа"""
    id: int
    created_at: datetime
    user_name: str
