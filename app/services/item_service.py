from sqlalchemy.orm import Session
from app.repositories.item_repo import ItemRepository
from app.schemas.item import ItemCreate

class ItemService:
    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 10):
        return ItemRepository.get_items(db, skip, limit)

    @staticmethod
    def create_item(db: Session, item: ItemCreate):
        return ItemRepository.create_item(db, item)