#!/usr/bin/python3

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "


    def do_create(self, line):
        pass

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
    pass

    def do_quit(self, arg):
        """Quit or EOF command to exit the program"""
        return True
     
    do_EOF = do_quit






if __name__ == '__main__':
    HBNBCommand().cmdloop()