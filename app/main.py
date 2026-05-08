from fastapi import FastAPI
from app.api.v1.items import router
from app.db.session import engine
from app.db.models.item import Item

# 创建数据库表
Item.metadata.create_all(bind=engine)

app = FastAPI(title="Phase B 分层架构项目")

# 注册路由
app.include_router(router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Phase B 已完成！分层架构搭建成功"}