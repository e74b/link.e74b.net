from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from peewee import SqliteDatabase, Model, TextField

app = FastAPI()
db = SqliteDatabase("db.sqlite3")

class Link(Model):
    code = TextField(unique=True)
    link = TextField()

    class Meta:
        database = db

db.create_tables([Link])

@app.get("/link/{code}")
def get_code(code: str):
    link = Link.get_or_none(Link.code == code)
    if link is None:
        return HTTPException(404)
    else:
        return RedirectResponse(link.link)


@app.post("/link/{code}")
def post_code(code: str, link: str = Form()):
    if Link.select().where(Link.code == code).exists():
        return HTTPException(403)
    link = Link(code=code, link=link)
    link.save()
    return {
            "status": "ok"
            }

