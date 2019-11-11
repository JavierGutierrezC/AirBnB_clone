#!/usr/bin/python3
import cmd
import models
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

''' Class Console'''



class HBNBCommand(cmd.Cmd):
    '''Command Cosole'''
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "City"]


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

    def do_destroy(self,args):
        arguments = args.split()
        if not args:
            print("** class name missing **")
        else:
            if arguments[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            else:
            #arguments = args.split()
                if len(arguments) > 1:
                    dict_n = storage.all()
                    obj_n = arguments[0] + "." + arguments[1]
                    #print(obj_n)
                    if obj_n in dict_n:
                        del dict_n[obj_n]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")


if __name__ == '__main__':
    interprete = HBNBCommand()
    interprete.cmdloop()
