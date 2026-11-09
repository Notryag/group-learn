from fastapi import FastAPI

# 创建应用，供 Uvicorn 加载。
app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
