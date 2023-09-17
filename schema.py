from pydantic import BaseModel

class Book(BaseModel):
    title:str
    class Config:
        orm_mode = True
