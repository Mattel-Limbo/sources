from typing import Union
from fastapi import FastAPI, HTTPException, Query
from src.webhook.discord import *
import json
from pydantic import BaseModel
from src.func.scrapper import scrape_attributes_with_values

app = FastAPI()

class Body(BaseModel):
    title: str
    description: str | None = None
    timestamp: str | None = None
    username: str | None = None
    avatar: str | None = None

class ElementAttributes(BaseModel):
    tag: str
    attributes: dict

class AttributeResponse(BaseModel):
    elements: list[ElementAttributes]

@app.post("/webhook/discord")
async def webhookSender(body: Body):
    return postToWebhook(body)

@app.get("/scrape", response_model=AttributeResponse)
async def scrapeAttributeEndpoints(url: str = Query(..., description="The URL to scrape for attributes and values")):
    try:
        elements = scrape_attributes_with_values(url)
        return AttributeResponse(elements=elements)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
