from fastapi import FastAPI, Request, Query, Body, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

app.mount("/static", StaticFiles(directory="statics"), name="statics")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/table", response_class=HTMLResponse)
async def table(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="table.html",
    )


@app.get("/items")
async def items(username: str = "Anonymous", age: int = 18):
    return {
        "message": f"hello {username}, age is {age}",
    }


@app.get("/welcome/", response_class=HTMLResponse)
async def welcome(request: Request, username: str = "Anonymous"):
    return templates.TemplateResponse(
        request=request, name="welcome.html", context={"username": username}
    )


@app.get("/welcome/{username}", response_class=HTMLResponse)
async def welcome(request: Request, username: str = "Anonymous"):
    return templates.TemplateResponse(
        request=request, name="welcome.html", context={"username": username}
    )


# listSubject = ["Digital Skill", "Web Programming", "Programming I", "Statistic"]
listSubject = [
    {"id": 1, "name": "Digital Skill"},
    {"id": 2, "name": "Web Programming"},
    {"id": 3, "name": "Programming I"},
    {"id": 4, "name": "Statistic"},
]


async def searchSubject(listSubject: list, keyword: str):
    return [word for word in listSubject if keyword in word["name"]]
    # response = []
    # for word in listSubject:
    #     if keyword in word:
    #         response.append(word)
    # return response


@app.get("/subject", response_class=HTMLResponse)
async def subject(request: Request, keyword: str | None = None):
    matchSubject = listSubject
    if keyword:
        matchSubject = await searchSubject(listSubject, keyword)

    return templates.TemplateResponse(
        request=request,
        name="subject.html",
        context={"subjectList": matchSubject},
    )


class Subject(BaseModel):
    id: int = Form()
    name: str = Form()


@app.post("/subject")
async def create_subject(
    request: Request,
    subject_id: Annotated[str, Form()],
    subject_name: Annotated[str, Form()],
):
    sub = {"id": subject_id, "name": subject_name}
    if not sub in listSubject:
        listSubject.append(sub)

    return templates.TemplateResponse(
        request=request,
        name="subject.html",
        context={"subjectList": listSubject},
    )


#     http   :// 127.0.0.1 : 8000 /items ?username=sornchai & age=20 parameter

#     https  :// fastapi.tiangolo.com /tutorial/path-params/
#    http :80 | https :443  | https = http + security
# python -m fastapi dev main.py
