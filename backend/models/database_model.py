from sqlmodel import SQLModel, Field
from datetime import date


class Department(SQLModel, table=True):
  
    department_id: int | None = Field(default=None, primary_key=True, description="部门ID")
    name: str


class User(SQLModel, table=True):

    user_id: int | None = Field(default=None, primary_key=True, description="用户ID")
    name: str 
    password: str
    email: str | None
    phone: str | None
    avatar: str | None
    role: str
    department_id: int | None = Field(default=None, foreign_key="department.department_id")
    
class Admin(SQLModel, table=True):
  
    admin_id: int | None = Field(default=None, primary_key=True, description="管理员ID")
    name: str
    password: str
    phone: str | None
    email: str | None
    avatar: str | None
    
class Course(SQLModel, table=True):
  
    course_id: int | None = Field(default=None, primary_key=True, description="课程ID")
    name: str
    teacher_id: int | None = Field(default=None, foreign_key="user.user_id")
    content: str | None
    start_time: date | None
    end_time: date | None

class Enrollment(SQLModel, table=True):
    
    enrollment_id: int | None = Field(default=None, primary_key=True, description="报名ID")
    user_id: int | None = Field(default=None, foreign_key="user.user_id")
    course_id: int | None = Field(default=None, foreign_key="course.course_id")
    
class Grade(SQLModel, table=True):
    
    grade_id: int | None = Field(default=None, primary_key=True, description="成绩ID")
    enrollment_id: int | None = Field(default=None, foreign_key="enrollment.enrollment_id")
    
    professional_score: float | None
    project_score: float | None
    promotion_score: float | None
    presentation_score: float | None
    
    total_score: float | None
    

class Project(SQLModel, table=True):

    project_id: int | None = Field(default=None, primary_key=True, description="项目ID")
    crouse_id: int | None = Field(default=None, foreign_key="course.course_id")
    name: str
    description: str | None
    team_members: str | None
    

    