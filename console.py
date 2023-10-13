#!/usr/bin/python3
"""
This is a module for the console module
Defines the class HBNBCommand
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
from shlex import split


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Terminates the console incase of the input is CTRL + D"""
        return True

    def emptyline(self):
        """Does not execute anything"""
        pass

    def help_quit(self):
        """Documentation for the help command"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """Documentation for the EOF command"""
        print("Exit the program using EOF (Ctrl+D)")

    def do_create(self, arg):
        """creates a new instance of and save it as a JSON file"""
        if not arg:
            print("** class name missing **")
            return
        if arg in HBNBCommand.classes:
            instance = HBNBCommand.classes[arg]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints the string representation of an instance"""
        args = split(arg)
        if not args:
            print("** class name mising ***")
            return
        if args[0] in HBNBCommand.classes:
            if len(args) < 2:
                print("** instance id missing **")
                return
            else:
                key = "{}.{}".format(args[0], args[1])
                objects = storage.all()
                print(objects.get(key, "** no instance found **"))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
