#!/usr/bin/python3


from models.base_model import BaseModel
import json
import datetime


class FileStorage:
    
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass


    def all(self):
        return FileStorage.__objects


    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
        
    def save(self):
        
        serialised_objects = {}
        
        for key, obj in FileStorage.__objects.items():
            serialised_objects[key] = obj.to_dict()
            
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialised_objects, file)


    def reload(self):
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
        dict = self.__dict__
        dict['__class__'] = self.__class__.__name__

        if 'created_at' in dict and isinstance(dict['created_at'], datetime):
            dict['created_at'] = dict['created_at'].isoformat()
        if 'updated_at' in dict and isinstance(dict['updated_at'], datetime):
            dict['updated_at'] = dict['updated_at'].isoformat()

        return dict


