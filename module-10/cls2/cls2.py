class Character:
    name = None
    x = None
    y = None
    hp = 100
    mp = 100

    def move(self):
        print('I am moving')

    def identify(self):
        print(self.name)
        self.move()


char_1 = Character()
char_1.name = 'Alex'
char_1.move()
char_1.identify()
