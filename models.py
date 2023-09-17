from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Book(Base):
    __tablename__='book'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)