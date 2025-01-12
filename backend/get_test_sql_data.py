import random
from db import get_session
from models.database_model import Department


# 添加学院测试信息
def get_fake_department():
    departments =   [
        "计算机科学与技术学院",
        "电子信息工程学院",
        "机械工程学院",
        "经济管理学院",
        "外国语学院",
        "法学院",
        "艺术学院",
        "建筑与土木工程学院",
        "化学与材料工程学院",
        "生命科学学院"
    ]
    for department in departments:
        data = Department(name=department)
        with get_session() as session:
            session.add(data)
            session.commit()
    return "ok"
    
if __name__ == '__main__':
    # print(get_fake_department())
    

    