-- 用户表，存储用户的基本信息
CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT, -- 用户ID，主键，自增
    username VARCHAR(255) UNIQUE NOT NULL, -- 用户名，唯一
    password VARCHAR(255) NOT NULL, -- 密码
    role ENUM('teacher', 'student') NOT NULL, -- 角色，教师或学生
    email VARCHAR(255), -- 邮箱
    avatar VARCHAR(255), -- 头像
    phone VARCHAR(255), -- 电话
    department_id INT, -- 部门ID，外键
    FOREIGN KEY (department_id) REFERENCES Department(department_id) -- 关联部门表
);

-- 管理员表，存储管理员的基本信息
CREATE TABLE Admin (
    admin_id INT PRIMARY KEY AUTO_INCREMENT, -- 管理员ID，主键，自增
    phone VARCHAR(255), -- 电话
    email VARCHAR(255), -- 邮箱
    name VARCHAR(255), -- 名字
    avatar VARCHAR(255), -- 头像
    password VARCHAR(255) NOT NULL -- 密码
);

-- 课程表，存储课程的基本信息
CREATE TABLE Course (
    course_id INT PRIMARY KEY AUTO_INCREMENT, -- 课程ID，主键，自增
    name VARCHAR(255) NOT NULL, -- 课程名称
    content TEXT, -- 课程内容
    start_date DATE, -- 开始日期
    end_date DATE, -- 结束日期
    cover VARCHAR(255), -- 课程封面
    teacher_id INT, -- 教师ID，外键
    FOREIGN KEY (teacher_id) REFERENCES User(user_id) -- 关联用户表
);

-- 选课表，存储学生选课信息
CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT, -- 选课ID，主键，自增
    student_id INT, -- 学生ID，外键
    course_id INT, -- 课程ID，外键
    FOREIGN KEY (student_id) REFERENCES User(user_id), -- 关联用户表
    FOREIGN KEY (course_id) REFERENCES Course(course_id) -- 关联课程表
);

-- 成绩表，存储学生的成绩信息
CREATE TABLE Grade (
    grade_id INT PRIMARY KEY AUTO_INCREMENT, -- 成绩ID，主键，自增
    enrollment_id INT, -- 选课ID，外键
    professional_score DECIMAL(5,2), -- 专业评分
    project_score DECIMAL(5,2), -- 项目评分
    promotion_score DECIMAL(5,2), -- 推广评分
    presentation_score DECIMAL(5,2), -- 路演评分
    FOREIGN KEY (enrollment_id) REFERENCES Enrollment(enrollment_id) -- 关联选课表
);

-- 项目表，存储课程项目的信息
CREATE TABLE Project (
    project_id INT PRIMARY KEY AUTO_INCREMENT, -- 项目ID，主键，自增
    course_id INT, -- 课程ID，外键
    description TEXT, -- 项目描述
    team_members TEXT, -- 团队成员
    FOREIGN KEY (course_id) REFERENCES Course(course_id) -- 关联课程表
);

-- 部门表，存储部门的信息
CREATE TABLE Department (
    department_id INT PRIMARY KEY AUTO_INCREMENT, -- 部门ID，主键，自增
    name VARCHAR(255) NOT NULL -- 部门名称
); 