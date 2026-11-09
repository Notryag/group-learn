from fastapi import FastAPI

# 创建应用，供 Uvicorn 加载。
app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}