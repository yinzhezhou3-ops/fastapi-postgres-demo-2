from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import APP_PORT, ENVIRONMENT


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行的代码
    print(f"Starting application in {ENVIRONMENT} mode")
    print("Database migrations should be run manually with: alembic upgrade head")
    yield
    # 关闭时执行的代码
    print("Shutting down application")


app = FastAPI(
    title="FastAPI Postgres Demo",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "ok", "environment": ENVIRONMENT}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=APP_PORT,
        reload=True,
    )
