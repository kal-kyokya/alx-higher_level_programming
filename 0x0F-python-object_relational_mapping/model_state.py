#!/usr/bin/python3
"""
'model_state' Creates a Class to be mapped to
a Database Table using 'declarative_base'
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Blueprint for the 'states' Table of our Database.

    Parent class:
        Base: Provides attributes and methods required
              for Object-Relational Mapping
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
