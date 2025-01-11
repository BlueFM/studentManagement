from fastapi import APIRouter
from backend.models.database_model import User, Department, Project, Course, Grade, Enrollment
from db import get_session

from sqlmodel import select

router = APIRouter()

# 查看所有院系
@router.get("/departments")
async def get_departments():
    with get_session() as session:
        query = select(Department)
        departments = session.exec(query).all()
    return departments

