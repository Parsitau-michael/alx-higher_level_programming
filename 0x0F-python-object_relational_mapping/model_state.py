#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

""" This module demonstrates the use of SQLAlchemy
"""


Base = declarative_base()


class State(Base):
    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)
