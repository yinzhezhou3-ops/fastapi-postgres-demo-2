from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models.item import Item

class ItemRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, item_data) -> Item:
        """创建物品"""
        db_item = Item(**item_data.model_dump())
        self.db.add(db_item)
        await self.db.commit()
        await self.db.refresh(db_item)
        return db_item

    async def get(self, item_id: int) -> Item | None:
        """根据 ID 获取物品"""
        result = await self.db.execute(
            select(Item).where(Item.id == item_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[Item]:
        """获取所有物品"""
        result = await self.db.execute(
            select(Item).offset(skip).limit(limit)
        )
        return result.scalars().all()
