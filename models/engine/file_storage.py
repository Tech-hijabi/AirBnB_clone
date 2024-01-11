#!/usr/bin/python3

import json

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
                for key, obj_dict in loaded_objects.item():
                    class_name, obj_id = key.spilt('.')
                    class_ = globals()[class_name]
                    obj = class_(**obj_dict)
                    FileStorage.__objects[key] = obj
                    
        except FileNotFoundError:
            pass