# AirBnB Clone

This project is an AirBnB clone. During the current stage of operation, the project files include the ability to create and examine several storage objects.

## Console

To begin using the program, simply use the command:
```bash
./console.py
```
and you will be greeted with the command prompt:
```bash
(hbnb)
```
The console also operates in non-interactive mode by passing in commands. We recommend starting with the following:
```bash
echo "help" | ./console.py
```
This command will list usable commands

## Usage
Simply type one of the following commands when the command prompt (hbnb) is showing to run the command.
running help will produce the following results:
```
Documented commands (type help <topic>):
========================================'
EOF  all  create  destroy  help  quit  show  update
```
EOF - End Of File - also entered as Ctrl + D, ends the command prompt
```
EOF
Ctrl + D
```
all - prints all stored objects, can be used to print all objects of a given class
```
all
all <classname>
```
create - creates an instance of a class, displays the id of the created object
```
create <classname>
```
destroy - destroys an instance of an object using the class name and id
```
destroy <classname> <id>
```
help - displays all commands (as above) or provides help on a specific command
```
help
help <command>
```
quit - exits the command prompt
```
quit
```
show - displays an instance of an object using class name and id
```
show <classname> <id>
```
update - updates an instance of an object using class name and id. value needs to be included in "quotes"
```
update <classname> <id> <attribute name(no quotes)> <value (quotes)>
```
Several commands can also be called using the format:
```
classname.command()
classname.command(arguments)
```
Usable commands include -
all() count(s) show("id") destroy("id") update("id", "attribute", "value")

All of these commands function as the version above. Count displays the number instances of the given class.

### Class
The following classes exist for the program:

BaseModel

User

Review

State

City

Place

Amenity


## Contributors
Corbin Vandeventer
Selidex Parnell

## License
This is an open source program
