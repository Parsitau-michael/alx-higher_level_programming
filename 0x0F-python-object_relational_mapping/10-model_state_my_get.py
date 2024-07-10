#!/usr/bin/python3

""" This module lists all state objects that contain a letter a from the db
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    username, password, db, state_name = argv[1], argv[2], argv[3], argv[4]

    """ Creating an engine and binding it to the session """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, db))
    """ Creating a configured session class """
    Session = sessionmaker(bind=engine)
    """ Creating a Session """
    session = Session()
    """ Querying all state Objects, ordered by id """
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
