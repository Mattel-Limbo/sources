from fastapi import APIRouter
from src.api.endpoints import webhook, scrape

api_router = APIRouter()
api_router.include_router(webhook.router, prefix="/webhook", tags=["webhook"])
api_router.include_router(scrape.router, prefix="/scrape", tags=["scrape"])