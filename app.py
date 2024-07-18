from typing import Union
from fastapi import FastAPI
from src.webhook.discord import *
import json
from pydantic import BaseModel

app = FastAPI()

class Body(BaseModel):
    title: str
    description: str | None = None
    timestamp: str | None = None
    username: str | None = None
    avatar: str | None = None

@app.post("/mattel-webhook")
async def webhookSender(body: Body): 
    return postToWebhook(body)


