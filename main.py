import os
from enum import Enum

import uvicorn
from fastapi import FastAPI
from models import Book as MBook
from fastapi_sqlalchemy import DBSessionMiddleware, db
import models
from schema import Book

app = FastAPI()
databenv=os.environ['DATABASE_URI']= 'postgresql+psycopg2://postgres:??@localhost:5433/Newdb'
app.add_middleware(DBSessionMiddleware, db_url=databenv)
@app.get("/")
async def root():
    return {"message": "Hello World"}

class ModelName(str,Enum):
    name1='ofer'
    name2='poler'
    name3='koper'

@app.get('/test/{name}')
async def get_name(name:ModelName):
    if name is ModelName.name1:
        return {'name':name}
    if name is ModelName.name2:
        return {'name':name}
    return {'name': name}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

equi=[{'eq1':'helm'},{'eq2':'boots'},{'eq3':'boot'}]

@app.get("/equipm")
async def eqi(param:int = 1 , maxpar:int=10):
    return equi[param : param+maxpar]


#get_from_db

@app.get('/new')
async def testdb():
    booktitle = db.session.query(MBook).all()
    return booktitle

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)


#post_in_db
@app.post('/addnew/', response_model=Book)
async def addbook(book: Book):
    bookdb=MBook(title=book.title)
    db.session.add(bookdb)
    db.session.commit()
    return bookdb