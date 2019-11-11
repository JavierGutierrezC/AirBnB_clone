#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

''' Class Console'''

list_class = ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]

dict_class = {"State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review, "User": User}

class HBNBCCommand(cmd.Cmd):
    '''Command Cosole'''
    

    prompt = "(hbnb) "

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
        if not args:
            print('** class name missing **')
        elif args not in list_class:
            print('** class doesn\'t exist **')
        else:
            element = dict_class[args]()
            print(element.id)
            element.save()
        
    def do_show(self, args):
        if not args:
            print('** class name missing **')
        elif args not in list_class:
            print('** class doesn\'t exist **')

        else:
            spl_args = args.split()
            if len(spl_args) < 2:
                print('** instance id missing **')

if __name__ == '__main__':
    interprete = HBNBCCommand()
    interprete.cmdloop()
