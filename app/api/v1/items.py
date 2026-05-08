from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.item import Item, ItemCreate
from app.services.item_service import ItemService
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/items", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return ItemService.get_items(db, skip, limit)

@router.post("/items", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return ItemService.create_item(db, item)