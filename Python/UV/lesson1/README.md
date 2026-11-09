# 一节课上手 uv

前提：已安装 uv，会运行简单的 Python 文件。目标：会创建项目、管理依赖、运行代码。

## 1. 常用命令

在项目目录执行：

| 操作 | 命令 | 类比前端 |
| --- | --- | --- |
| 初始化新项目 | `uv init` | `npm init` |
| 安装项目依赖 | `uv sync` | `npm install` |
| 添加依赖 | `uv add requests` | `npm install 包名` |
| 删除依赖 | `uv remove requests` | `npm uninstall 包名` |
| 运行 Python 文件 | `uv run main.py` | 运行程序 |
| 指定项目 Python 版本 | `uv python pin 3.12` | 指定运行时版本 |

`requests` 是发送 HTTP 请求的第三方库，这里仅用来演示依赖管理。`uv add/remove` 会同时更新依赖配置、锁文件和环境。

新建项目的完整流程（在准备存放项目的目录执行）：

```powershell
uv init my-demo
cd my-demo
uv add requests
uv run main.py
```

已有项目通常只需 `uv sync`，日常启动用 `uv run main.py`。`uv run` 也会自动检查并同步依赖。

## 2. 认识三个文件

| 文件或目录 | 作用 | 提交到 Git？ |
| --- | --- | --- |
| `pyproject.toml` | 项目配置和依赖清单，类似 `package.json` | 是 |
| `uv.lock` | 依赖精确版本，类似 `package-lock.json` | 是 |
| `.venv/` | 项目独立环境，存放解释器入口和安装的依赖 | 否 |

独立环境让不同项目的依赖互不干扰，uv 会自动管理，不必手动激活。

**`uv venv` 只创建环境，不安装项目依赖；`uv sync` 会自动创建环境并安装依赖，所以通常不需要先执行 `uv venv`。**

`uv sync` 报找不到 `pyproject.toml` 时，先检查目录；全新项目先执行 `uv init`。

## 3. 运行本课示例

本课已配置好项目，不需要再执行 `uv init`。从仓库根目录运行：

```powershell
cd Python/UV/lesson1
uv sync
uv run main.py
```

预期输出：

```text
你好，uv！
当前 Python： ...\lesson1\.venv\Scripts\python.exe
```

`main.py` 的 `greet(name)` 返回问候文字；`sys.executable` 显示实际使用的 Python 路径，`sys` 是 Python 自带模块，不用安装。脚本打印后退出；Web 服务需要由代码另行启动。

## 4. 小练习

在本课目录执行 `uv add requests`，观察配置中的依赖变化，再用 `uv remove requests` 删除它。

补全 `exercise1.py` 中的 `learning_message(tool)`，返回 `我正在学习 ` 加工具名。提示：使用 `f"我正在学习 {tool}"` 这样的字符串格式，在函数中返回结果。

```powershell
uv run exercise1.py
```

完成标准：输出 `我正在学习 uv` 和 `我正在学习 FastAPI` 两行，并能说清 `sync` 和 `run` 的区别。当前状态：已介绍，待完成练习。

参考：[uv 官方项目指南](https://docs.astral.sh/uv/guides/projects/)。
