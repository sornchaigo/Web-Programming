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


class Subject(BaseModel):
    id: int
    name: str


# listSubject = ["Digital Skill", "Web Programming", "Programming I", "Statistic"]
listSubject: list[Subject] = [
    # {"id": 1, "name": "Digital Skill"},
    # {"id": 2, "name": "Web Programming"},
    # {"id": 3, "name": "Programming I"},
    # {"id": 4, "name": "Statistic"},
    Subject( id= 1, name= "Digital Skill"),
    Subject( id= 2, name= "Web Programming"),
    Subject( id= 3, name= "Programming I"),
    Subject( id= 4, name= "Statistic"),
]


async def searchSubject(listSubject: list, keyword: str):
    return [word for word in listSubject if keyword in word.name]


@app.get("/api/subject")
async def getSubject(keyword: str | None = ""):
    return [word for word in listSubject if keyword in word.name]


@app.post("/api/subject/create")
async def createSubject(subject: Subject):
    # listSubject.append({"id": subject.id, "name": subject.name})
    listSubject.append(subject)
    return [subject]


@app.get("/subject", response_class=HTMLResponse)
async def subject(request: Request, keyword: str | None = None):
    newlist = sorted(listSubject, key=lambda d: d.name)
    matchSubject = newlist
    if keyword:
        matchSubject = await searchSubject(listSubject, keyword)

    return templates.TemplateResponse(
        request=request,
        name="subject.html",
        context={"subjectList": matchSubject, "keyword": keyword},
    )


@app.post("/subject")
async def create_subject(
    request: Request,
    subject_id: Annotated[int, Form()],
    subject_name: Annotated[str, Form()],
):
    global listSubject
    sub = {"id": subject_id, "name": subject_name}
    if not sub in listSubject:
        listSubject.append(sub)
        listSubject = sorted(listSubject, key=lambda d: d.id)

    return templates.TemplateResponse(
        request=request,
        name="subject.html",
        context={"subjectList": listSubject},
    )


#     http   :// 127.0.0.1 : 8000 /items ?username=sornchai & age=20 parameter

#     https  :// fastapi.tiangolo.com /tutorial/path-params/
#    http :80 | https :443  | https = http + security
# python -m fastapi dev main.py
