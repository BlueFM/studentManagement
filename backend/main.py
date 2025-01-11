from fastapi import FastAPI
from backend.db import create_db_and_tables
from apps.router import router  # 假设 router.py 中定义了 router 对象
import asyncio

app = FastAPI()


# 添加健康检查路是
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# 包含 router.py 中的路由
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

