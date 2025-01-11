CREATE TABLE department (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE user (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'teacher', 'student') NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    avatar VARCHAR(255),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE course (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    content TEXT,
    start_date DATE,
    end_date DATE,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES user(user_id)
);

CREATE TABLE enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES user(user_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

CREATE TABLE grade (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT,
    professional_score DECIMAL(5,2),
    project_score DECIMAL(5,2),
    promotion_score DECIMAL(5,2),
    presentation_score DECIMAL(5,2),
    FOREIGN KEY (enrollment_id) REFERENCES enrollment(enrollment_id)
);

CREATE TABLE project (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    description TEXT,
    team_members TEXT,
    FOREIGN KEY (course_id) REFERENCES course(course_id)
); 