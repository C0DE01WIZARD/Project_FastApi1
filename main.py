from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def function():
    a = "Hello, Python"
    return {"message": a}


@app.post("/post")
async def function():
    pass
    passsss