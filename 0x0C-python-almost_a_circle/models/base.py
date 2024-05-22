#!/usr/bin/python3
"""
'base' is a class creation module
"""
import json


class Base:
    """Blueprint for all instances of type Base.

    Class Attribute:
        nb_objects: Number of intialized instances.
    """

    nb_objects = 0

    def __init__(self, input_id=None):
        """Constructs and Initializes instances of class Base.

        Arg:
            input_id: ID number associated with each instance.
        """
        if input_id is None:
            Base.nb_objects += 1
            self.__id = Base.nb_objects
        else:
            self.__id = input_id

    @property
    def id(self):
        """Getter for the attribute 'id'.

        The setter follows right after.
        """
        return (self.__id)

    @id.setter
    def id(self, input_value):
        self.__id = input_value
        return (self.__id)

    @staticmethod
    def to_json_string(listOfDicts):
        """Returns a JSON format of the input list of dictionaries.

        Arg:
            listOfDicts: A list of one or many dictionaries.
        """
        lst = listOfDicts
        if lst is None or len(lst) == 0:
            return ("[]")
        return (json.dumps(lst))

    @classmethod
    def save_to_file(cls, listOfObjs):
        """Writes a JSON repr. of a list into a json file.

        Arg:
            listOfObjs: A list of one or many class instance.
        """
        with open("Rectangle.json", "w") as json_file:
            if listOfObjs is None or len(listOfObjs) == 0:
                pass
            else:
                listOfDicts = []
                for obj in listOfObjs:
                    listOfDicts.append(cls.to_dictionary(obj))
                json.dump(listOfDicts, json_file)
