from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv(dotenv_path='.env')

# 从环境变量中获取数据库连接信息
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

# 拼装数据库连接字符串
DATABASE_URL = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
# print(DATABASE_URL)
# 引擎
engine = create_engine(DATABASE_URL, echo=True)

# 创建数据库表
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)

if __name__ == "__main__":
    create_db_and_tables()