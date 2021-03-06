#This is a basic Stack data structure usin OOP programming in python.
#A stack is a data structure which uses a LIFO(Last In First Out) order to preform operations.
#Last In First Out means that the last item to be added to the stack will be the first one to be taken out
#It is used in many cases. For example internet search history and creating programming languages.
#This program is a bare bones version but can be improved and added to
#Python implements a Stack by using a list. 
#The list contains all the information held in the stack and we use python list functions within our stack methods.
class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, arg):
        self.l.append(arg)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def __len__(self):
        return len(self.l)

    def is_empty(self):
        return len(self) == 0
