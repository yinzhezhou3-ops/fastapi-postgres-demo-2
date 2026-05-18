from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.item_service import ItemService
from app.schemas.item import ItemCreate, ItemResponse
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=ItemResponse)
async def create_item(
    item: ItemCreate,
    db: AsyncSession = Depends(get_db)
):
    """创建新物品"""
    service = ItemService(db)
    return await service.create_item(item)


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(
    item_id: int,
    db: AsyncSession = Depends(get_db)
):
    """根据 ID 获取物品"""
    service = ItemService(db)
    item = await service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/", response_model=list[ItemResponse])
async def get_all_items(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """获取所有物品"""
    service = ItemService(db)
    return await service.get_all_items(skip, limit)
