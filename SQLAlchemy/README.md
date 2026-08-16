# SQLAlchemy 学习计划

本目录用于通过一个小型“学习小组管理系统”学习 SQLAlchemy 2.x。

课程协作和教学规则见仓库根目录的 [agent.md](../agent.md)。

## 学习目标

- 理解 `Engine`、`Connection`、`Session` 和事务
- 使用 SQLAlchemy Core 表达 SQL
- 使用 ORM 定义模型和表关系
- 完成可靠的增删改查
- 编写连接、聚合、分页和关联查询
- 使用 Alembic 管理数据库结构变化
- 了解 Web 项目中的 Session 生命周期、测试和性能优化

## 学习模式

本课程分为两条路线，默认先走快速学习，再根据实际需要进入深入学习。

### 快速学习：先获得基本使用能力

目标是尽快能够在项目中使用 SQLAlchemy，不要求一开始理解所有底层机制。

快速路线只掌握：

- 如何连接数据库
- 如何定义模型和创建表
- 如何新增、查询、修改和删除数据
- 如何使用基本条件查询、排序和分页
- 如何建立最常用的一对多和多对多关系
- 如何正确提交和回滚事务
- 如何在项目中组织数据库代码

快速路线暂时不深入：Core 内部实现、复杂加载策略、连接池细节、异步机制、性能分析和 ORM 源码。

快速路线完成标准：能够独立完成一个简单的数据库 CRUD 模块，并能解释每段代码的基本作用。

### 深入学习：理解原理和边界

目标是理解 SQLAlchemy 的设计、不同 API 的差异以及生产环境中的取舍。

深入路线会学习：

- Core 和 ORM 的关系
- 查询语句、结果对象和对象映射过程
- Session、事务和对象状态
- 关系加载策略与 N+1 查询
- Alembic 数据库迁移
- 连接池、并发、性能和批量操作
- 异步 API、测试和 Web 框架集成

深入路线完成标准：能够分析 SQLAlchemy 生成的 SQL，定位常见问题，并根据场景选择合适的 API。

## 当前路线

当前先采用“快速学习”模式。每完成一个核心任务，再补充必要的概念；快速路线结束后，再决定是否进入深入路线。

## 学习约定

- 使用 Python 3.11+
- 使用 SQLAlchemy 2.x 的现代写法
- 先使用 SQLite，降低环境准备成本
- 先学习同步 API，再学习异步 API
- 每一节都包含：概念、可运行示例、练习和复习

SQLAlchemy 2.x 推荐使用 `select()` 查询，并将 Core 与 ORM 结合学习。官方入口可参考：[SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)。

## 快速学习路线

| 章节 | 主题 | 学完后能够 |
| --- | --- | --- |
| 1 | 连接和第一个模型 | 连接 SQLite、定义模型、创建表 |
| 2 | Session 基础 | 新增数据、提交事务、查询单条数据 |
| 3 | 基本 CRUD | 完成增删改查和简单条件查询 |
| 4 | 查询结果和常用查询 | 理解查询结果，完成排序、分页和多条件查询 |
| 5 | 基本表关系 | 使用一对多和多对多关系 |
| 6 | 项目化使用 | 抽离数据库配置，处理事务和基本异常 |
| 7 | 小型综合项目 | 完成学习小组管理系统的核心功能 |

## 深入学习路线

| 章节 | 主题 | 主要内容 |
| --- | --- | --- |
| 1 | 第一个数据库程序 | 安装、Engine、SQLite、模型、建表、查询 |
| 2 | SQLAlchemy Core | `Table`、`MetaData`、插入、更新、删除、连接 |
| 3 | ORM 模型 | `DeclarativeBase`、`Mapped`、`mapped_column`、约束 |
| 4 | Session 与 CRUD | `Session`、提交、回滚、对象状态 |
| 5 | 表关系 | 一对多、多对多、`relationship()`、级联 |
| 6 | 查询进阶 | JOIN、聚合、子查询、分页、动态条件 |
| 7 | 加载策略 | 懒加载、`selectinload()`、`joinedload()`、N+1 |
| 8 | 事务与工程实践 | 事务边界、异常处理、连接池、日志 |
| 9 | Alembic | migration、升级、回滚、数据迁移 |
| 10 | Web 项目集成 | Repository、Service、FastAPI Session 依赖 |
| 11 | 异步 SQLAlchemy | `AsyncEngine`、`AsyncSession`、异步驱动 |
| 12 | 测试与性能 | pytest、测试数据库、索引、批量操作、EXPLAIN |
| 13 | 综合项目 | 完成学习小组管理系统 |

## 示例项目模型

后续课程会逐步建立这些模型：

- `User`：用户
- `StudyGroup`：学习小组
- `Membership`：用户与小组的成员关系
- `Note`：学习笔记

## 目录说明

```text
SQLAlchemy/
├── README.md
└── lesson1/
    ├── README.md
    ├── database.py
    ├── exercise1.py
    └── main.py
```

从 [第 1 节课程](lesson1/README.md) 开始学习。
