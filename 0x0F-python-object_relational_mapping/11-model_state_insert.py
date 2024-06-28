#!/usr/bin/python3
"""
'11-model_state_insert' adds a row to a Database table
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    new_state = State(name="Nigeria")
    session.add(new_state)
    session.commit()
