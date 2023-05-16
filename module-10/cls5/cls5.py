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
        self.damage = 10

    def kick(self):
        return self.damage


class Knife(Weapon):
    def __init__(self):
        self.damage = 5

    def throw(self):
        return self.damage - 2


class Sword(Weapon):
    def __init__(self):
        self.damage = 15


class Axe(Weapon):
    def __init__(self):
        self.damage = 20


knife = Knife()
print(knife.damage)
print(knife.kick())
print(knife.throw())
sword = Sword()
print(sword.damage)
print(sword.kick())
