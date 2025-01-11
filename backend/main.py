from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from apps.router import router
import asyncio

app = FastAPI()


# 添加健康检查路是
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# 包含 router.py 中的路由
app.include_router(router)

# 跳转到doc
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    
    import dotenv
    import os
    import uvicorn
    
    dotenv.load_dotenv()
    DEBUG = os.getenv("DEBUG")
    print(f"DEBUG: {DEBUG}")
    if DEBUG == "True":
        host_addr = "127.0.0.1"
    else:
        host_addr = "0.0.0.0"
    # uvicorn.run(app, host=host_addr, port=8000, reload=True)
    
    # 调用系统 执行 uvicorn main:app --host {host_addr} --port 8000 --reload 命令
    import sys
    sys.exec(f"uvicorn.run(app, host='{host_addr}', port=8000, reload=True)")
    

