from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/health")
def health():
    # TODO：返回一个字典，让接口输出 {"status": "ok"}。
    return {"status": "ok"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/users/{user_id}")
async def get_user(user_id:int = Path(..., title="用户ID", description="用户的唯一标识符", ge=1)):
    return {"user_id": user_id, "name": f"User {user_id}"}