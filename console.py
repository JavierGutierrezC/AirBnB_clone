#!/usr/bin/python3
import cmd
import models
import shlex
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
''' Class Console'''


class HBNBCommand(cmd.Cmd):
    '''Command Cosole'''
    prompt = "(hbnb) "
    class_list = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity,
                  "Place": Place, "Review": Review}

    def emptyline(self):
        '''Goes to the next line'''
        pass

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''End of file'''
        return True

    def do_create(self, args):
        '''Creates a new Instance of BaseModel'''
        arguments = args.split(" ")
        if not arguments[0]:
            print("** class name missing **")
            pass
        elif arguments[0] in HBNBCommand.class_list:
            new = eval(arguments[0])()
            print(new.id)
            models.storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''Prints the string representation of the instance'''
        arguments = args.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            dict_n = storage.all()
            obj_n = arguments[0] + "." + arguments[1]
            if obj_n in dict_n.keys():
                print(dict_n[obj_n])
            else:
                print("** no instance found **")

    def do_update(self, args):
        '''Updates the instance based on its class name and id'''
        arguments = shlex.split(args)
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif("{}.{}".format(arguments[0],
                            arguments[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(arguments) == 2:
            print("** attribute name missing **")
        elif len(arguments) == 3:
            print("** value missing **")
        else:
            dict_n = storage.all()
            obj_n = arguments[0] + "." + arguments[1]
            if obj_n in dict_n.keys():
                new_attribute = getattr(dict_n[obj_n], arguments[2], "")
                setattr(dict_n[obj_n], arguments[2],
                        type(new_attribute)(arguments[3]))
                dict_n[obj_n].save()

    def do_all(self, args):
        '''Prints a string of all instances based or not on class name'''
        if args == "":
            list1 = list(storage.all().values())
            print(list(map(lambda x: str(x), list1)))
        elif args in HBNBCommand.class_list:
            list1 = list(storage.all().values())
            list2 = filter(lambda x: type(x) is
                           HBNBCommand.class_list.get(args), list1)
            print(list(map(lambda x: str(x), list2)))
        elif args not in HBNBCommand.class_list:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id'''
        arguments = args.split()
        if not args:
            print("** class name missing **")
        else:
            if arguments[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            else:
                if len(arguments) > 1:
                    dict_n = storage.all()
                    obj_n = arguments[0] + "." + arguments[1]
                    if obj_n in dict_n:
                        del dict_n[obj_n]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")

    def default(self, args):
        """ default method for aditional functions """
        args1 = (args.replace('.', ' ').replace('(', ' ').replace(')', ' '))
        args2 = args1.split()
        if len(args2) > 1:
            cmd = args2.pop(1)
            new_dic = re.split(r"\s(?![^{]*})", args1)
        args3 = ' '.join(args2).replace(',', '')
        try:
            eval('self.do_' + cmd + '(args3)')
        except:
            print("** invalid Syntax **")

if __name__ == '__main__':
    interprete = HBNBCommand()
    interprete.cmdloop()
