import pathlib

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
print((BASE_DIR / "templates").exists())
print(BASE_DIR / "templates")

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def home_view(request: Request):
    print(request)
    return templates.TemplateResponse(request, "home.html", context={"person": "John"})


@app.post("/")
async def home_detail_view():
    return {"msg": "FooBar"}
