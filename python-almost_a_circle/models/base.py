#!/usr/bin/python3
"""
This module contains the Base class
This class will be the base of all other classes in the project.
The goal of it is to manage id attribute in all your future classes
"""
import os
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class

        Parameters:
        id (int): id of the Base object, defaults to None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        # Creating a dummy instance for Rectangle or Square
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        # Updating the dummy instance with the dictionary values
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []

        with open(filename, 'r') as file:
            instances_dict = cls.from_json_string(file.read())

        return [cls.create(**instance) for instance in instances_dict]
