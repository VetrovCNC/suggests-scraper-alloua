from sqlalchemy import (
    create_engine,
    Column, Integer, Text
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

from config import DB_STRING


db = create_engine(DB_STRING)
Base = declarative_base()


class Suggests(Base):
    __tablename__ = 'suggests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, unique=True)
    query = Column(Text)
    suggests = Column(Text)

Session = sessionmaker(db)
session = Session()

Base.metadata.create_all(db)
