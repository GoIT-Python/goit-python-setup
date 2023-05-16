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

    def damage_right(self):
        self.right_hand.kick()

    def damage_left(self):
        self.left_hand.kick()

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

    def kick(self):
        print('Knife Kick')
        return self.damage


class Sword(Weapon):
    def __init__(self):
        self.damage = 15

    def kick(self):
        print('Sword Kick')
        return self.damage


class Axe(Weapon):
    def __init__(self):
        self.damage = 20

    def kick(self):
        print('Axe Kick')
        return self.damage


class Gun(Weapon):
    def __init__(self):
        self.damage = 20

    def kick(self):
        print('Gun Kick')
        return self.damage


char = Character('char')
knife = Knife()
char.pick_weapon(knife)
print(char.left_hand)
# print(char.right_hand)
char.damage_left()
sword = Sword()
char.pick_weapon((sword))
print(char.left_hand)
print(char.right_hand)
char.damage_right()
