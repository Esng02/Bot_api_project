from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.models import get_db
from app.crud import create_message, get_messages

app = FastAPI()


class Message(BaseModel):
    author: str
    content: str


@app.get("/api/v1/messages/", response_model=List[Message])
async def read_messages(skip: int = 0, limit: int = 10):
    """
    Возвращает список сообщений с пагинацией.
    - skip: количество сообщений, которые нужно пропустить
    - limit: максимальное количество сообщений для возврата
    """
    db = get_db()
    messages = get_messages(db, skip=skip, limit=limit)
    return messages


@app.post("/api/v1/message/")
async def post_message(message: Message):
    """
    Создает новое сообщение.
    - message: объект сообщения с автором и содержанием
    """
    db = get_db()
    create_message(db, message)
    return {"message": "Message created successfully"}


