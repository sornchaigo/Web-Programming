from fastapi import FastAPI, Request, Query, Path, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from typing import Annotated
from enum import Enum

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


# @app.get("/items")
# async def items(username: str = "Anonymous", age: int = 18):
#     return {
#         "message": f"hello {username}, age is {age}",
#     }


# @app.get("/welcome/", response_class=HTMLResponse)
# async def welcome(request: Request, username: str = "Anonymous"):
#     return templates.TemplateResponse(
#         request=request,
#         name="welcome.html",
#         context={"username": username},
#     )


@app.get("/welcome/{username}", response_class=HTMLResponse)
async def welcome(request: Request, username: str = "Anonymous"):
    return templates.TemplateResponse(
        request=request,
        name="welcome.html",
        context={"username": username},
    )


class ModelName(str, Enum):
    assist = "Assistant Professor"
    assoc = "Associate Professor"
    prof = "Professor"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.prof:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "Associate Professor":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(
#     skip: int = 0,
#     limit: int = 10,
#     q: list[str] = Query(default="BUU", min_length=2),
# ):
#     if q:
#         item = {"q": q}
#         fake_items_db.append(item)
#     return fake_items_db[skip : skip + limit]


@app.post("/items/{item_id}")
async def read_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=1000)],
    q: str | None = None,
    short: bool = False,
    other: Annotated[int, Body(ge=1)] = 0,  # other:int = Field(ge=1, description="Other Value")
):
    print(other)
    item = {"item_id": item_id}
    if q:
        item["q"] = q
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    if other:
        item.update({"other": other})
    fake_items_db.append(item)
    return fake_items_db


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    item.tax = item.price * 0.07
    print(item)
    print(*item)
    print({**item.dict()})
    return item
