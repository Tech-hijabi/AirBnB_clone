#!/usr/bin/python3
"""
FileStorage Module

This module defines FileStorage class, which is responsible for serializing
and deserializing instances of different classes to and from a JSON file.

Attributes:
    __file_path (str): The path to the JSON file where data will be stored.
    __objects (dict): A dictionary to store serialized objects
    by their unique key.

Methods:
    __init__(self): Initializes a new instance of the FileStorage class.
    all(self): Returns the dictionary of all serialized objects.
    new(self, obj): Adds a new object to the storage dictionary.
    save(self): Serializes and saves the storage dictionary to the JSON file.
"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import datetime


class FileStorage:
    """
    FileStorage Class

    This class handles the serialization and deserialization of instances
    of different classes to and from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initialize a new instance of the FileStorage class.
        """
        pass

    def all(self):
        """
        Return the dictionary of all serialized objects.

        Returns:
            dict: The dictionary containing all serialized objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the storage dictionary.

        Args:
            obj: An object to be serialized and stored.

        Returns:
            None
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize and save the storage dictionary to the JSON file.

        Returns:
            None
        """
        serialised_objects = {}

        for key, obj in FileStorage.__objects.items():
            serialised_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialised_objects, file)

    def reload(self):
        """
        Deserialize and load objects from the JSON file to storage dictionary.

        This method reads the content of the JSON file, deserializes objects,
        and updates the storage dictionary with the loaded objects.

        Returns:
            None
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    class_ = globals()[class_name]
                    obj = class_(**obj_dict)
                    FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

    def to_dict(self):
        """
        Convert the instance attributes to a dictionary for serialization.

        This method converts instance attributes to dictionary representation,
        suitable for serialization to JSON. It also ensures datetime objects
        are represented in ISO format.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        dict_ = self.__dict__
        dict_['__class__'] = self.__class__.__name__

        if 'created_at' in dict_ and isinstance(dict_['created_at'], datetime):
            dict_['created_at'] = dict_['created_at'].isoformat()
        if 'updated_at' in dict_ and isinstance(dict_['updated_at'], datetime):
            dict_['updated_at'] = dict_['updated_at'].isoformat()

        return dict_
