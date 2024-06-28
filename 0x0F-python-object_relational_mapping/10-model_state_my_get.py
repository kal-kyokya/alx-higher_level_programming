#!/usr/bin/python3
"""
'10-model_state_my_get' match an input name with table rows.
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

    states = session.query(State).filter(State.name == sys.argv[4]).all()
    if len(states) > 0:
        for state in states:
            print(f"{state.id}")
    else:
        print("Not found")
