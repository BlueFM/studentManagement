from fastapi import APIRouter
from models.database_model import User, Department, Project, Course, Grade, Enrollment
from models.response_model import ResponseModel
from db import get_session

from sqlmodel import select

router = APIRouter()

# 查看所有院系
@router.get("/departments", response_model=ResponseModel)
async def get_departments():
    with get_session() as session:
        query = select(Department)
        departments = session.exec(query).all()
    return ResponseModel(code=200, message="success", data=departments)

# 添加院系
@router.post("/departments", response_model=ResponseModel)
async def add_department(department: Department):
    with get_session() as session:
        session.add(department)
        session.commit()
        session.refresh(department)
    return ResponseModel(code=200, message="add success", data=department)

# 按关键字搜索院系
@router.get("/departments/search", response_model=ResponseModel)
async def search_department(keyword: str):
    with get_session() as session:
        query = select(Department).where(Department.name.like(f"%{keyword}%"))
        departments = session.exec(query).all()
    return ResponseModel(code=200, message="success", data=departments)

# 删除院系
@router.delete("/departments/{id}", response_model=ResponseModel)
async def delete_department(id: int):
    with get_session() as session:
        department = session.get(Department, id)
        if department:
            session.delete(department)
            session.commit()
            return ResponseModel(code=200, message="delete success")
        else:
            return ResponseModel(code=404, message="department not found")

