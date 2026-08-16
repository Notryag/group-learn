"""第 1 题：修改用户姓名。

先运行一次 main.py，确保 learning.db 和 users 表已经创建。
然后补全 update_user_name() 函数，再运行本文件。
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from database import User, engine


def update_user_name(user_id: int, new_name: str) -> None:
    """将指定用户的姓名修改为 new_name。

    练习要求：
    1. 创建 Session
    2. 使用 select() 查询用户
    3. 使用 session.scalar() 获取用户对象
    4. 修改用户姓名
    5. 提交事务
    """
    pass

    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.scalar(statement)
        if user is not None:
            user.name = new_name
            session.commit()
        

if __name__ == "__main__":
    update_user_name(1, "Alice Chen")

    with Session(engine) as session:
        user = session.scalar(select(User).where(User.id == 1))

        assert user is not None, "找不到 id 为 1 的用户，请先运行 main.py"
        assert user.name == "Alice Chen", "姓名还没有修改成功"

        print(f"练习通过：{user}")


def inspect_user_rows() -> None:
    """第 2 题：观察 execute() 返回的完整查询结果。"""
    # 练习要求：
    # 1. 创建 Session
    # 2. 创建 statement = select(User)
    # 3. 使用 session.execute(statement)
    # 4. 打印 result.all()
    # 5. 遍历结果，打印每一行的 type(row) 和 row
    # 本题暂时不要使用 scalar() 或 scalars()。
    with Session(engine) as session:
        statement = select(User)
        result = session.execute(statement)
        rows = result.all()
        print(f"查询结果：{rows}")
        print("遍历结果：")
        for row in rows:
            print(f"  type(row): {type(row)}, row: {row}")


if __name__ == "__main__":
    inspect_user_rows()


def get_user_by_id(user_id: int) -> User | None:
    """第 3 题：使用 scalar() 查询一个用户。"""
    # 练习要求：
    # 1. 创建 Session
    # 2. 创建 select(User).where(User.id == user_id)
    # 3. 使用 session.scalar(statement)
    # 4. 返回查询结果
    # 本题暂时不要使用 scalars()。
    pass


if __name__ == "__main__":
    user = get_user_by_id(1)
    assert user is not None, "找不到 id 为 1 的用户"
    print(f"scalar() 查询结果：{user}")
