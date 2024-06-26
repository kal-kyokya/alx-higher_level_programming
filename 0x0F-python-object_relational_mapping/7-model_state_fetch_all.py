#!/usr/bin/python3
"""
'7-model_state_fetch_all' Retrieves all
states stored inside the 'State Table'
"""
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
