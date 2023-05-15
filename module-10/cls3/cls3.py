import random


class Character:
    count = 0
    hp = 100
    mp = 100

    def __init__(self, name):
        Character.count += 1
        self.name = name
        self.x = random.randint(0, 100)
        self.y = random.randint(0, 100)

    def move(self):
        print('I am moving')

    def identify(self):
        print(self.name)


char_1 = Character('Baltasar')
# char_2 = Character()
# char_3 = Character()
print(char_1.x)
print(Character.count)
print(char_1.y)
