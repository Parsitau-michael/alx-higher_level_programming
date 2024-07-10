#!/usr/bin/python3

""" This module demonstrates the use of SQLAlchemy
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ This module represents the State Class
    """
    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)
