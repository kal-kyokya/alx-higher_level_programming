#!/usr/bin/python3
"""
'6-model_state' Create a database Engine and its Table(s)
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[0], sys.argv[1], sys.argv[2],),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
