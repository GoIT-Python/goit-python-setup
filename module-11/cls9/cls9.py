class Character:
    def __init__(self, name):
        self.name = name  # public
        self._damage = 10  # protected
        self.__hp = 100  # private

    def __getitem__(self):
        return self.__hp

    def __setitem__(self, value):
        if 0 < value <= 100:
            self.__hp = value


char = Character('Jack')
print(char.__getitem__())
char.__setitem__(90)
print(char.__getitem__())
