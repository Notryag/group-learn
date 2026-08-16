from sqlalchemy import select, text
from sqlalchemy.orm import Session

from database import User, engine, initialize_database


def main() -> None:
    # 先验证应用可以通过 Engine 连接数据库。
    with engine.connect() as connection:
        database_check = connection.execute(text("SELECT 1")).scalar_one()
        print(f"数据库连接成功：{database_check}")

    # 初始化逻辑单独放在 init_db.py 中。
    initialize_database()

    # 使用 SQLAlchemy 2.x 推荐的 select() 风格查询。
    with Session(engine) as session:
        statement = select(User).order_by(User.id)
        print(f"执行 SQL 查询：{statement}")
        result = session.execute(statement)
        rows = result.all()
        print(f"查询结果：{rows}")

        print("当前用户：")
        for row in rows:
            user = row[0]
            print(f"- {user}")


if __name__ == "__main__":
    main()
