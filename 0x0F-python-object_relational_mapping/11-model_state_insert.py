#!/usr/bin/python3

""" This module adds a record to the states table using SQLAlchemy
"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, desc
from sys import argv


if __name__ == "__main__":
    username, password, db = argv[1], argv[2], argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    obj1 = State(name="Louisiana")
    session.add(obj1)
    session.commit()

    state = session.query(State).order_by(desc(State.id)).first()

    if state:
        print("{}".format(state.id))

    session.close()
