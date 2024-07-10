#!/usr/bin/python3

""" This module lists all state objects that contain a letter a from the db
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    username, password, db = argv[1], argv[2], argv[3]

    """ Creating an engine and binding it to the session """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, db))
    """ Creating a configured session class """
    Session = sessionmaker(bind=engine)
    """ Creating a Session """
    session = Session()
    """ Querying all state Objects, ordered by id """
    states = session.query(State).filter(State.name.
                                         like('%a%')).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
