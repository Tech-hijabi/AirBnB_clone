#!/usr/bin/python3


from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from shlex import split
import cmd
import re
import sys


def parse(arg):
    
    squares = re.search(r"\[(.*?)\]", arg)
    curls = re.search(r"\{(.*?)\}", arg)
    if curls is None:
        if squares is None:
            return [i.strip(",") for i in split(arg)]
        else:
            isol = split(arg[:squares.span()[0]])
            parti = [i.strip(",") for i in isol]
            parti.append(squares.group())
            return parti
    else:
        isol = split(arg[:curls.span()[0]])
        parti = [i.strip(",") for i in isol]
        parti.append(curls.group())
        return parti

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }


    def do_create(self, arg):
       
        line_arg = parse(arg)
        print(line_arg)
        if len(line_arg) == 0:
            print("** class name missing **")
        elif line_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(line_arg[0])().id)
            storage.save()
            

    def do_show(self, arg):
        line_arg = parse(arg)
        obj_dict = storage.all()
    
        if len(line_arg) == 0:
            print("** class name missing **")
        elif line_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        
        elif len(line_arg) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(line_arg[0], line_arg[1]) not in obj_dict:
            print("** no instance found **")
            
        else:
            print("{}.{}".format(line_arg[0], line_arg[1]))
            
    def do_destroy(self, arg):
        line_arg = parse(arg)
        obj_dict = storage.all()
        
        if len(line_arg) == 0:
            print("** class name missing **")
        elif line_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        
        elif len(line_arg) == 1:
            print("** instance id missing **")
            
        elif "{}.{}".format(line_arg[0], line_arg[1]) not in obj_dict:
            print("** no instance found **")            

        else:
            del obj_dict["{}.{}".format(line_arg[0], line_arg[1])]
            storage.save()

    def do_all(self, arg):
        line_arg = parse(arg)
        
        if len(line_arg) > 0 and line_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        else:
            obj_list = []
            combined_values = storage.all().values()
            for obj in combined_values:
                if len(line_arg) > 0 and line_arg[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(line_arg) == 0:
                    obj_list.append(obj.__str__())
                    
            print(obj_list)

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_EOF(self, arg):
        """EOF or quit command to exit program"""
        return True
     
    do_quit = do_EOF






if __name__ == '__main__':
    HBNBCommand().cmdloop()