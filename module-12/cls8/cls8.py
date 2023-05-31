import pickle
from copy import copy, deepcopy


class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.a = 123
        self.bag = ['potion', 'money']

    def add_to_bag(self, item):
        self.bag.append(item)

    def __copy__(self):
        copy_obj = Character(self.name)
        return copy_obj

    def __deepcopy__(self, memodict=None):
        if memodict is None:
            memodict = {}
        obj = Character(self.name)
        memodict[id(self)] = obj

        for k, v in self.__dict__.items():
            setattr(obj, k, deepcopy(v, memodict))

        return obj


char = Character('Jack')
char.add_to_bag(['big apple', ])
# print(char)
# print(char.name)
# print(char.hp)
print(id(char.bag[2]))

# char_copy = copy(char)
# print(char_copy)
# print(char_copy.name)
# print(char_copy.hp)
# print(char_copy.bag)

char_copy = deepcopy(char)
# print('char_copy', char_copy)
print(id(char_copy.bag[2]))
