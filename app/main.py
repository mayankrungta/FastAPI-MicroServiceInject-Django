from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home_view():
    return {"message": "Hello World"}


@app.post("/")
async def home_detail_view():
    return {"msg": "FooBar"}
