#!/usr/bin/python3
"""
'8-model_state_fetch_first' Retrieves a table element
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    state = session.query(State).first()
    if state is None:
        print("Empty table")
    else:
        print(f"{state.id}: {state.name}")
