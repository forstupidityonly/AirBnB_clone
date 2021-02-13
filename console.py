#!/usr/bin/python3
"""console"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """class for console"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing"""
        pass

    def do_quit(self, args):
        """Quit to exit"""
        return True

    def do_EOF(self, args):
        """EOF to exit"""
        pass
        return True

    def do_create(self, *args):
        """Creates a new instance of BaseModel, and saves it"""
        if args == "" or args is None:
            print("** class name missing **")
        elif args[0] not in models.class_dict:
            print("** class doesn't exist **")
        else:
            func = models.class_dict[args[0]]
            temp = func()
            temp.save()
            print(temp.id)

    def do_show(self, *args):
        """Prints the string representation of an instance based on the class name and id"""
        if args == "" or args is None:
            print("** class name missing **")
        elif args[0] not in models.class_dict:
            print("** class doesn't exits **")
        else:
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
