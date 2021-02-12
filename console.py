#!/usr/bin/python3
"""console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for console"""
    prompt = "(hbnb) "

    def emptyline(self):
        """do nothing"""
        pass

    def do_quit(self, args):
        """quit to exit"""
        return True

    def do_EOF(self, args):
        """eof to exit"""
        pass
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
