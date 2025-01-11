from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date
from decimal import Decimal

class Department(SQLModel, table=True):
    department_id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    role: str
    email: Optional[str] = None
    phone: Optional[str] = None
    department_id: Optional[int] = Field(default=None, foreign_key="department.department_id")

class Course(SQLModel, table=True):
    course_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    content: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    teacher_id: Optional[int] = Field(default=None, foreign_key="user.user_id")

class Enrollment(SQLModel, table=True):
    enrollment_id: Optional[int] = Field(default=None, primary_key=True)
    student_id: Optional[int] = Field(default=None, foreign_key="user.user_id")
    course_id: Optional[int] = Field(default=None, foreign_key="course.course_id")

class Grade(SQLModel, table=True):
    grade_id: Optional[int] = Field(default=None, primary_key=True)
    enrollment_id: Optional[int] = Field(default=None, foreign_key="enrollment.enrollment_id")
    professional_score: Optional[Decimal] = None
    project_score: Optional[Decimal] = None
    promotion_score: Optional[Decimal] = None
    presentation_score: Optional[Decimal] = None

class Project(SQLModel, table=True):
    project_id: Optional[int] = Field(default=None, primary_key=True)
    course_id: Optional[int] = Field(default=None, foreign_key="course.course_id")
    description: Optional[str] = None
    team_members: Optional[str] = None 