class Character:
    def __init__(self, name):
        self.name = name  # public
        self._damage = 10  # protected
        self.__hp = 100  # private

    @property
    def hp(self):
        print('GETTER')
        return self.__hp

    @hp.setter
    def hp(self, value):
        print('SETTER')
        if 0 < value < 100:
            self.__hp = value
        else:
            raise ValueError('HP should be in range 1-100')


char = Character('Noah')
print(char.hp)
char.hp = 77
print(char.hp)
