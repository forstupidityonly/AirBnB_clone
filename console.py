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

    def default(self, args):
        """default run"""
        x = args.split(".")
        y = x[1].split("(")
        if x[0] not in models.class_dict or len(x) < 2:
            print("*** Unknown syntax: {}".format(args))
            return
        elif x[1] == "all()":
            self.do_all(x[0])
        elif x[1] == "count()":
            self.count(x[0])
        elif y[0] == "show":
            j = y[1].split('"')
            args = x[0] + " " + j[1]
            self.do_show(args)
        elif y[0] == "destroy":
            j = y[1].split('"')
            args = x[0] + " " + j[1]
            self.do_destroy(args)
        else:
            print("*** Unknown syntax: {}".format(args))
            return

    def count(self, args):
        """counts number of instances of a class"""
        sdict = models.storage.all()
        count = 0
        for y in sdict:
            z = y.split(".")
            if z[0] == args:
                count += 1
        print(count)

    def do_quit(self, args):
        """Quit to exit"""
        return True

    def do_EOF(self, args):
        """EOF to exit"""
        return True

    def do_create(self, args):
        """Creates a new instance of a class, and saves it"""
        if not args or args is None:
            print("** class name missing **")
            return
        x = args.split()
        if x[0] not in models.class_dict:
            print("** class doesn't exist **")
            return
        else:
            func = models.class_dict[x[0]]
            temp = func()
            print(temp.id)
            models.storage.save()

    def do_show(self, args):
        """Prints a class"""
        if args == "" or args is None:
            print("** class name missing **")
            return
        x = args.split()
        if x[0] not in models.class_dict:
            print("** class doesn't exist **")
        elif len(x) < 2:
            print("** instance id missing **")
        else:
            sdict = models.storage.all()
            fb = 0
            for y in sdict:
                z = y.split(".")
                if z[0] == x[0]:
                    if z[1] == x[1]:
                        fb = 1
                        print(sdict[y])
            if fb == 0:
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id"""
        if args == "" or args is None:
            print("** class name missing **")
            return
        x = args.split()
        if x[0] not in models.class_dict:
            print("** class doesn't exist **")
        elif len(x) < 2:
            print("** instance id missing **")
        else:
            sdict = models.storage.all()
            fb = 0
            for y in sdict:
                z = y.split(".")
                if z[0] == x[0]:
                    if z[1] == x[1]:
                        fb = 1
                        var = y
            if fb == 1:
                del sdict[var]
                models.storage.save()
            if fb == 0:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all classes"""
        pdict = models.storage.all()
        if args == "" or args is None:
            lc = []
            for key in pdict:
                lc.append(str(pdict[key]))
            print(lc)
        else:
            x = args.split()
            if x[0] not in models.class_dict:
                print("** class doesn't exist **")
            else:
                lc = []
                for key in pdict:
                    z = key.split(".")
                    if z[0] == x[0]:
                        lc.append(str(pdict[key]))
                print(lc)

    def do_update(self, args):
        """Update a class based on id"""
        if args == "" or args is None:
            print("** class name missing **")
            return
        x = args.split()
        if x[0] not in models.class_dict:
            print("** class doesn't exist **")
        elif len(x) < 2:
            print("** instance id missing **")
        elif len(x) < 3:
            print("** attribute name missing **")
        elif len(x) < 4:
            print("** value missing **")
        else:
            sdict = models.storage.all()
            fb = 0

            str_cat = x[3]
            if not x[3].endswith('"'):
                for i in range(4, len(x)):
                    str_cat += " " + x[i]
                    if x[i].endswith('"'):
                        break
            if not str_cat.endswith('"'):
                print("** value missing **")
                return
            str_cat = str_cat.split('"')

            for y in sdict:
                z = y.split(".")
                if z[0] == x[0]:
                    if z[1] == x[1]:
                        fb = 1
                        var = y
            if fb == 1:
                var2 = x[2]
                if var2 in sdict[var].__dict__:
                    var3 = type(sdict[var].__dict__[var2])
                    sdict[var].__dict__[var2] = var3(str_cat[1])
                sdict[var].__dict__[var2] = str_cat[1]
                sdict[var].save()
                models.storage.save()
            if fb == 0:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
