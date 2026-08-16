# 第 1 节：连接数据库并创建第一个模型

## 本节目标

完成本节后，你应该能够：

- 安装 SQLAlchemy
- 创建数据库引擎 `Engine`
- 连接 SQLite 数据库
- 使用 ORM 定义一个 `User` 模型
- 创建表并插入数据
- 使用 `select()` 查询数据
- 通过日志观察 SQLAlchemy 生成的 SQL

## 1. 安装依赖

在项目根目录执行：

```bash
python -m pip install "SQLAlchemy>=2.0,<3.0"
```

检查安装结果：

```bash
python -c "import sqlalchemy; print(sqlalchemy.__version__)"
```

## 2. 运行示例

进入本节目录：

```bash
cd SQLAlchemy/lesson1
python main.py
```

第一次运行时，`database.py` 中的初始化函数会在当前目录创建 `learning.db`、创建 `users` 表，并插入两条用户数据。因为示例打开了 `echo=True`，终端还会显示 SQLAlchemy 实际执行的 SQL。

再次运行不会重复插入数据。本地生成的 `learning.db` 只是练习数据库，不需要提交到 Git。

## 3. 核心代码

查询示例见同目录的 [`main.py`](main.py)，数据库配置和模型见 [`database.py`](database.py)。关键模型如下：

```python
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)


engine = create_engine("sqlite:///learning.db", echo=True)
Base.metadata.create_all(engine)
```

## 4. 代码理解

项目中将职责分开：

```text
database.py    数据库连接、Base、ORM 模型、建表和初始数据
main.py        连接验证和查询示例
exercise1.py   留给你的练习
```

`main.py` 只调用 `initialize_database()`，不直接写初始化细节。这样后续接入 Web 应用时，可以单独决定何时执行初始化逻辑。

### `create_engine()`

```python
engine = create_engine("sqlite:///learning.db", echo=True)
```

`Engine` 是应用程序和数据库之间的入口。这里使用 SQLite，数据库文件名是 `learning.db`。

`echo=True` 会打印 SQL 日志，学习阶段建议打开，这样可以把 Python 代码和实际 SQL 对照起来。

### `DeclarativeBase`

```python
class Base(DeclarativeBase):
    pass
```

所有 ORM 模型都继承这个基类。`Base.metadata` 会收集模型对应的表结构。

### `Mapped` 和 `mapped_column`

```python
id: Mapped[int] = mapped_column(primary_key=True)
```

这表示模型有一个整数类型的主键字段。SQLAlchemy 2.x 使用类型注解表达 Python 类型和数据库映射。

### `Session`

```python
with Session(engine) as session:
    session.add(user)
    session.commit()
```

`Session` 负责对象与数据库之间的交互。`add()` 将对象加入当前会话，`commit()` 才会真正提交事务。

### `select()` 和 `scalars()`

在学习 `scalars()` 之前，先观察完整的查询结果：

```python
statement = select(User)
result = session.execute(statement)
rows = result.all()
```

这里的 `result` 还不是 `User` 列表，而是包含查询行的结果对象。查询 `User` 时，每一行通常类似 `(User(...),)`。

完成 `exercise1.py` 中的 `inspect_user_rows()` 后，再看下面的简化写法：

```python
statement = select(User).order_by(User.id)
users = session.scalars(statement).all()
```

`select(User)` 构造查询语句，`scalars()` 将查询结果转换成 `User` 对象序列。

## 5. 动手练习

第 1 题和第 2 题都在 [`exercise1.py`](exercise1.py) 中。第 1 题的 `update_user_name()` 已经完成；现在请完成 `inspect_user_rows()`，不要直接看答案。

运行方式：

```bash
python main.py
python exercise1.py
```

第 1 题完成后，程序应该输出：

```text
练习通过：User(id=1, name='Alice Chen', email='alice@example.com')
```

第 2 题要求观察类似下面的结果：

```text
(User(id=1, name='Alice Chen', email='alice@example.com'),)
(User(id=2, name='Bob', email='bob@example.com'),)
```

注意：每一行是一个 `Row`，不是直接的 `User` 对象。完成第 2 题后，我们再解释 `scalar()` 和 `scalars()` 的区别。

### 第 3 题：使用 `scalar()` 查询一个用户

完成 `exercise1.py` 中的 `get_user_by_id()` 函数。

本题只学习 `scalar()`：它用于从查询结果中取得第一行的第一个字段。因为这里查询的是 `User`，所以返回一个 `User` 对象或 `None`。

暂时不要使用 `scalars()`，完成并提交第 3 题后再学习它。

完成第 1 题后，再尝试下面的扩展练习。请在 `User` 模型中增加一个字段：

```python
city: Mapped[str] = mapped_column(default="Shanghai")
```

然后完成以下任务：

1. 新增一个用户
2. 查询所有用户
3. 只查询名字为 `Alice` 的用户
4. 按用户姓名排序
5. 观察终端中对应的 SQL

提示：条件查询可以这样写：

```python
select(User).where(User.name == "Alice")
```

## 6. 常见问题

### 为什么修改模型后，旧表不会自动增加字段？

`Base.metadata.create_all()` 只负责创建不存在的表，不负责修改已有表结构。后续学习 Alembic 后，使用 migration 管理结构变化。

### 为什么必须调用 `commit()`？

SQLAlchemy 的写操作在事务中进行。没有提交，程序结束或 Session 关闭时，新增数据可能会被回滚。

### 为什么要使用 `with Session(engine)`？

上下文管理器可以在代码块结束时关闭 Session，减少连接没有释放的问题。

## 本节小结

本节建立了四个基本概念：

```text
Engine       连接数据库的入口
Base         ORM 模型的基类
Model        Python 类与数据库表的映射
Session      执行查询和提交事务的工作单元
```

下一节将学习 SQLAlchemy Core，直接使用 `Table` 和 SQL 表达式操作数据库。
