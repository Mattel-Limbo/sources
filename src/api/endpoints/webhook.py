from fastapi import APIRouter
from pydantic import BaseModel
from src.webhook.discord import post_to_webhook

router = APIRouter()

class Body(BaseModel):
    title: str
    description: str | None = None
    timestamp: str | None = None
    username: str | None = None
    avatar: str | None = None

@router.post("/discord", tags=["webhook"])
async def webhook_sender(body: Body):
    return post_to_webhook(body)