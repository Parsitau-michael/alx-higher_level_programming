#!/usr/bin/python3

""" This module creates a class definition of city
"""


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ This module represents the City Class
    """
    __tablename__ = 'cities'

    id = Column("id", Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey('states.id'),
                      nullable=False)
