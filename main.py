from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

app = FastAPI()

# 改回异步引擎（之前为了 Alembic 临时用了同步）
ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
engine = create_async_engine(ASYNC_DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI + PostgreSQL!"}

@app.get("/health")
async def health_check():
    try:
        async with AsyncSessionLocal() as session:
            await session.execute("SELECT 1")
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
