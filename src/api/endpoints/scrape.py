from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from src.func.scrapper import scrape_attributes_with_values

router = APIRouter()

class ElementAttributes(BaseModel):
    tag: str
    attributes: dict
    
class AttributeResponse(BaseModel):
    elements: list[ElementAttributes]

# Scrape the attributes and values from the provided URL and return them as a list of ElementAttributes.
@router.get("/", response_model=AttributeResponse, tags=["scrape"])
async def scrape_attribute_endpoints(url: str = Query(..., description="The URL to scrape for attributes and values")):
    try:
        elements = scrape_attributes_with_values(url)
        return AttributeResponse(elements=elements)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))