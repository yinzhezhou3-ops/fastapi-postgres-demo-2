from sqlalchemy.orm import Mapped, mapped_column
from app.models import Base

class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    description: Mapped[str | None] = None