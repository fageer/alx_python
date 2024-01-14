from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

""" create State class"""
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, 
                primary_key=True, 
                autoincrement=True, 
                unique=True, 
                nullable=False)
    name =  Column(String(128),
                   nullable=False)
