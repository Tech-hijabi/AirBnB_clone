#!/usr/bin/python3


from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
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
            zipped_values = storage.all().values()
            for obj in zipped_values:
                if len(line_arg) > 0 and line_arg[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(line_arg) == 0:
                    obj_list.append(obj.__str__())
                    
            print(obj_list)
            
    def do_update(self, arg):
        line_arg = parse(arg)
        obj_dict = storage.all()

        if len(line_arg) == 0:
            print("** class name missing **")
            return False

        elif line_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

            
        elif len(line_arg) == 1:
            print("** instance id missing **")
            return False

        elif "{}.{}".format(line_arg[0], line_arg[1]) not in obj_dict:
            print("** no instance found **")


        elif len(line_arg) == 2:
            print("** attribute name missing **")
            return False

        
        elif len(line_arg) == 3:
            try:
                type(eval(line_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        
        if len(line_arg) == 4:
            obj = obj_dict["{}.{}".format(line_arg[0], line_arg[1])]
            
            if line_arg[2] in obj.__class__.__dict__.__keys():
                value_type = type(obj.__class__.__dict__[line_arg[2]])
                obj.__dict__[line_arg[2]] =  value_type(line_arg[3])
                
        elif type(eval(line_arg[2])) == dict:
            obj = obj_dict["{}.{}".format(line_arg[0], line_arg[1])]
            for k, v in eval(line_arg[2]).items():
                if (k in obj.__class__.__dict__.keys() and 
                    type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_EOF(self, arg):
        """EOF or quit command to exit program"""
        return True
     
    do_quit = do_EOF






if __name__ == '__main__':
    HBNBCommand().cmdloop()