from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float


@router.post("/items")
async def create_item(item: Item):
    return {"message": "created", "data": item}
