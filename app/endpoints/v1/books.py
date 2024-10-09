from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.handlers.databases import get_mongo_db
from app.repositories.books import Book
from app.schemas.books import BookCreateInput, BookCreateOutput

router = APIRouter()


# @router.get("/", response_model=List[Book])


@router.post("/", response_model=BookCreateOutput)
async def create_book():
    book = await Book().save(data=BookCreateInput)
    return book
