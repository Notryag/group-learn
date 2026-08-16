"""第 1 节共用的数据库配置和 ORM 模型。"""

from pathlib import Path

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


DATABASE_PATH = Path(__file__).with_name("learning.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"


class Base(DeclarativeBase):
    """所有 ORM 模型的基类。"""


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120), unique=True)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name!r}, email={self.email!r})"


engine = create_engine(DATABASE_URL, echo=True)
[SQLAlchemy 2.0 文档](https://docs.sqlalchemy.org.cn/en/20/index.html)

def create_tables() -> None:
    """创建还不存在的表。"""
    Base.metadata.create_all(engine)


def seed_initial_users() -> None:
    """仅在 users 表为空时插入初始用户。"""
    with Session(engine) as session:
        has_user = session.scalar(select(User.id).limit(1)) is not None

        if not has_user:
            session.add_all(
                [
                    User(name="Alice", email="alice@example.com"),
                    User(name="Bob", email="bob@example.com"),
                ]
            )
            session.commit()
            print("已插入两条用户数据。")


def initialize_database() -> None:
    """完成数据库初始化。"""
    create_tables()
    seed_initial_users()


__all__ = [
    "Base",
    "User",
    "engine",
    "create_tables",
    "seed_initial_users",
    "initialize_database",
]
