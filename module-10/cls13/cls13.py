from collections import UserList, UserDict, UserString
from random import randint


class MyList(UserList):

    def say_hello(self):
        print(f'Hello from {self.data}')

    def update_with_random(self):
        self.data[0] = randint(0, 10)


a = MyList('klsnklnnkt')
# print(a)
a.append()
# a.say_hello()
a.update_with_random()
print(a)
