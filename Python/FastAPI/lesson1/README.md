# 第一个 FastAPI 接口

## 目标和前置知识

本节只解决一个问题：如何让浏览器请求执行 Python 函数，并收到返回的数据。

需要先认识 Python 的导入、函数和字典。如果这些语法还不熟悉，可以先围绕下面的示例学习。

## 新知识

- **HTTP 请求和 GET**：浏览器访问网址时会向服务端发送请求；GET 表示读取数据。
- **接口和路由**：接口是服务提供的访问入口；路由把请求的方法、路径与处理函数对应起来，例如 `GET /`。
- **JSON**：用于传输数据的文本格式，例如 `{"message": "Hello, FastAPI!"}`。FastAPI 能把函数返回的 Python 字典转成 JSON 响应。
- **Uvicorn**：运行 Web 应用的服务器程序，负责监听端口并接收请求；FastAPI 负责处理请求。

## 先理解最小例子

普通 Python 函数也能返回字典：

```python
def hello():
    return {"message": "Hello, FastAPI!"}
```

直接调用 `hello()` 会得到这个字典，但浏览器还不能访问它。`main.py` 为它增加了应用和路由：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}
```

1. `from fastapi import FastAPI` 导入创建应用的工具。
2. `FastAPI()` 创建应用对象，保存到 `app`，稍后交给服务器运行。
3. `@app.get("/")` 是装饰器写法：把紧随其后的函数注册为 `GET /` 的处理函数。注册时不会执行函数体。
4. 请求到达 `/` 时，框架调用 `hello()`，把返回字典转换为 JSON，默认返回 HTTP 状态码 `200`，表示成功。

这里使用普通 `def` 即可，异步语法留到后续学习。

## 安装和运行

需要安装 uv，项目要求 Python 3.10 或更新版本。下面是 Windows PowerShell 命令，先从仓库根目录进入本节目录：

```powershell
cd Python/FastAPI/lesson1
uv sync
uv run main.py
```

`uv sync` 向上找到 `FastAPI/pyproject.toml`，根据其中的依赖声明和 `uv.lock` 安装依赖，自动管理 `FastAPI/.venv` 环境。可以将 `pyproject.toml` 类比为前端的 `package.json`，将 `uv.lock` 类比为依赖锁文件。

首次准备执行 `uv sync`；日常开发在 `lesson1` 目录执行 `uv run main.py` 即可，不需要手动激活环境。`uv run` 也会在运行前检查并同步项目依赖。

`main.py` 末尾的启动代码：

```python
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
```

`if __name__ == "__main__"` 确保仅在直接执行文件时启动服务，被服务器导入时不会重复启动。`uvicorn.run()` 启动服务器，参数含义如下：

- `main:app`：加载当前目录 `main.py` 文件中的 `app` 对象。
- `reload=True`：修改代码后自动重新加载，适用于本地学习。
- 默认地址是 `127.0.0.1:8000`，仅本机访问。终端会持续运行；按 `Ctrl+C` 停止服务。

先预测访问结果，再打开 <http://127.0.0.1:8000/>，预期返回：

```json
{"message": "Hello, FastAPI!"}
```

打开 <http://127.0.0.1:8000/docs> 可看到自动生成的交互文档。展开 `GET /`，点击 **Try it out → Execute**，应看到状态码 `200` 和同样的数据。

将示例中的消息文字改一次，保存并刷新网页，观察响应变化。

常见问题：在其他目录启动可能找不到文件或无法导入 `main`，应先回到 `lesson1`；访问未注册的路径会返回 `404`；若端口被占用，可将启动代码中的 `port=8000` 改为 `port=8001`，并访问对应端口。若 `uv sync` 提示找不到 `pyproject.toml`，请确认位于本目录或它的项目父目录中。

## 练习：健康检查接口

编辑 `exercise1.py`，只补全 `health()` 函数体，不改路径与函数名。让 `GET /health` 返回：

```json
{"status": "ok"}
```

提示：参考示例中返回字典的方式，修改键和值。

停止示例服务后，在同一个 `lesson1` 目录启动练习：

```powershell
uv run uvicorn exercise1:app --reload
```

完成标准：访问 <http://127.0.0.1:8000/health> 得到上述 JSON，在 `/docs` 中执行该接口得到 `200`，并能解释装饰器和返回字典各自的作用。

当前仅介绍了应用、GET 路由与 JSON 返回，尚未确认掌握。完成练习后再学习参数，让客户端能够传入不同的数据。本节暂不涉及数据库、登录和项目分层。
