from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    listItems = ["Programming I", "Math", "Static", "Introduction to Industry"]
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"listItems": listItems},
    )
