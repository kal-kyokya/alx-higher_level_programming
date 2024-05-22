#!/usr/bin/python3
"""
'base' is a class creation module
"""
import json
import os

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
        with open(f"{cls.__name__}.json", "w") as json_file:
            listOfDicts = []
            if listOfObjs is None or len(listOfObjs) == 0:
                pass
            else:
                for obj in listOfObjs:
                    listOfDicts.append(cls.to_dictionary(obj))
            cls.to_json_string(listOfDicts)
            json.dump(listOfDicts, json_file)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dictionaries from the JSON format.

        Arg:
            json_string: A JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns a instance basd on the input dictionary.

        Arg:
            dictionary: Collection of attributes to be assigned.
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        else:
            new_obj = cls(1)

        new_obj.update(**dictionary)
        return (new_obj)

    @classmethod
    def load_from_file(cls):
        """Reads a JSON repr. into a list from a json file."""
        obj_list = []
        filename = f"{cls.__name__}.json"

        if os.path.exists(filename) is False:
            return obj_list

        with open(filename, "r") as json_file:
            dictionary_list = json.load(json_file)
            for obj in dictionary_list:
                obj_list.append(cls.create(**obj))
            return obj_list
