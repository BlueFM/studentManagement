import asyncio
from db import create_db_and_tables, async_engine, get_async_session
from model import Department
from sqlmodel import select

async def main():
    # 创建数据库表
    # await create_db_and_tables()
    print("数据库表已创建")

    # 插入数据
    async with get_async_session() as session:
        # 创建一个新的 Department 实例
        new_department = Department(name="计算机系")
        
        # 添加到会话
        session.add(new_department)
        
        # 提交事务
        await session.commit()
        
        # 刷新以获取新插入数据的 ID
        await session.refresh(new_department)
        
        print(f"插入的系名称: {new_department.name}, ID: {new_department.department_id}")

    # 关闭引擎
    await async_engine.dispose()

if __name__ == "__main__":
    asyncio.run(main()) 