from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.item_repo import ItemRepository
from app.schemas.item import ItemCreate, ItemResponse
from app.db.models.item import Item

class ItemService:
    def __init__(self, db: AsyncSession):
        self.repo = ItemRepository(db)

    async def create_item(self, item: ItemCreate) -> ItemResponse:
        """创建物品"""
        db_item = await self.repo.create(item)
        return ItemResponse.model_validate(db_item)

    async def get_item(self, item_id: int) -> ItemResponse | None:
        """获取单个物品"""
        db_item = await self.repo.get(item_id)
        if db_item:
            return ItemResponse.model_validate(db_item)
        return None

    async def get_all_items(self, skip: int = 0, limit: int = 100) -> list[ItemResponse]:
        """获取所有物品"""
        db_items = await self.repo.get_all(skip, limit)
        return [ItemResponse.model_validate(item) for item in db_items]
