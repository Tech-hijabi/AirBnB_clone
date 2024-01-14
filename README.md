# AirBnB Clone

AirBnB Clone is a project that recreates the core functionality of the AirBnB platform. It allows users to create, manage, and review various types of accommodation. It also provides a simple command interpreter for manipulating data without a visual interface.

## Command Interpreter

The command interpreter is a console application that allows users to perform CRUD operations on the data stored in a JSON file. It supports the following commands:

- **create**: Creates a new instance of a given class and saves it to the JSON file.
- **show**: Prints the string representation of an instance based on its class and id.
- **destroy**: Deletes an instance based on its class and id.
- **all**: Prints all string representations of instances of a given class or of all classes.
- **update**: Updates an attribute of an instance based on its class and id.

### How to start it

To start the command interpreter, run the following command in your terminal:

```bash
./console.py
```

You will see a prompt `(hbnb)` where you can type commands.

### How to use it

To use the command interpreter, type a command followed by its arguments. For example:

```bash
(hbnb) create BaseModel
(hbnb) show BaseModel 1234-1234-1234
(hbnb) update User 4321-4321-4321 email "airbnb@holbertonshool.com"
```

You can also use a different syntax for some commands, where you put the class name and the arguments in quotes. For example:

```bash
(hbnb) "BaseModel".all()
(hbnb) "User".count()
(hbnb) "Place".destroy("89fc26d9-17d2-4587-ad63-6b4d3a81e8a4")
```

For more information about each command, type `help` followed by the command name.

### Examples

Here are some examples of using the command interpreter:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) create User
b6a6e15a-d9c3-4c74-b927-0298a4f1b02b
(hbnb) show User b6a6e15a-d9c3-4c74-b927-0298a4f1b02b
[User] (b6a6e15a-d9c3-4c74-b927-0298a4f1b02b) {'id': 'b6a6e15a-d9c3-4c74-b927-0298a4f1b02b', 'created_at': datetime.datetime(2024, 1, 14, 9, 9, 26, 54386), 'updated_at': datetime.datetime(2024, 1, 14, 9, 9, 26, 54386)}
(hbnb) update User b6a6e15a-d9c3-4c74-b927-0298a4f1b02b first_name "Saheed"
(hbnb) show User b6a6e15a-d9c3-4c74-b927-0298a4f1b02b
[User] (b6a6e15a-d9c3-4c74-b927-0298a4f1b02b) {'id': 'b6a6e15a-d9c3-4c74-b927-0298a4f1b02b', 'created_at': datetime.datetime(2024, 1, 14, 9, 9, 26, 54386), 'updated_at': datetime.datetime(2024, 1, 14, 9, 9, 26, 54386), 'first_name': 'Saheed'}
(hbnb) "User".count()
1
(hbnb) quit
$
```

## Authors

- Saheed Kehinde Yusuf
- Barakat Mohammed
