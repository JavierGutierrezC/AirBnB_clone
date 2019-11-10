#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage

''' Class Console'''


class HBNBCommand(cmd.Cmd):
    '''Command Cosole'''
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User"]

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
        models.storage.reload()
        if len(args) < 1:
            print("** class name missing **")
            pass
        else:
            arguments = args.split(" ")
            if arguments[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            else:
                if len(arguments) < 2:
                    print("** instance id missing **")
                    return
                else:
                    dict_n = storage.all()
                    obj_n = arguments[0] + "." + arguments[1]
                    if obj_n in dict_n.keys():
                        print(dict_n[obj_n])
                    else:
                        print("** no instance found **")

if __name__ == '__main__':
    interprete = HBNBCommand()
    interprete.cmdloop()
