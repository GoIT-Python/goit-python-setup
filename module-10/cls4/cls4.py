# SOLID:

# Single responsibility (SRP)

import random


class Character:
    hp = 100
    mp = 100

    def __init__(self, name):
        self.left_hand = None
        self.right_hand = None
        self.name = name
        self.x = random.randint(0, 100)
        self.y = random.randint(0, 100)

    def pick_weapon(self, weapon):
        if not self.left_hand:
            self.left_hand = weapon
        elif not self.right_hand:
            self.right_hand = weapon
        else:
            print('I am full')

    def show_weapon(self):
        return self.left_hand, self.right_hand

    def move(self):
        print('I am moving')

    def identify(self):
        print(self.name)

    def die(self):
        return self.left_hand, self.right_hand


class Weapon:
    def __init__(self):
        self.type = 'sword'
        self.damage = 10


char_1 = Character('char_1')
char_2 = Character('char_2')
sword = Weapon()
print(sword.type)
print(sword.damage)
char_1.pick_weapon(sword)
print(char_1.left_hand)
char_1.die()
print(char_1.right_hand)
