from typing import Annotated
import pandas as pd

from fastapi import FastAPI, Request
from fastapi import File, UploadFile, Form

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from io import BytesIO
app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/upload", StaticFiles(directory="uploads"), name="upload")
uploadFiles = []


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    print(uploadFiles)
    return templates.TemplateResponse(
        request=request, name="index.html", context={"uploadFiles": uploadFiles, "test": "test"}
    )


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    files: list[UploadFile], name: Annotated[str | None, Form()] = None
):

    try:

        # single file
        # contents = file.file.read()
        # with open(f"uploads/{name}", "wb") as upFile:
        #     upFile.write(contents)

        for file in files:
            contents = await file.read()
            with open(f"uploads/{file.filename}", "wb") as upFile:
                upFile.write(contents)
                uploadFiles.append(file.filename)

    except Exception as ex:
        return {"message": f"There was an error uploading the file {ex}"}

    return {
        "name": name,
        # "filename": file.filename,
        # "file_size": file.size,
        # "file_type": file.content_type,
    }

@app.post("/csv/")
async def upload_csv(files: UploadFile):
    try:
        contents = await files.read()
        df = pd.read_csv(BytesIO(contents), delimiter=',')

    except Exception as ex:
        return {"message": f"There was an error uploading the file {ex}"}
    return df.to_dict()
