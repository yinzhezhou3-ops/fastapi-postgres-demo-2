from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)  # 添加这个字段
    description = Column(String, nullable=True)  # 改为 nullable
