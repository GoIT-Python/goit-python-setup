# public
# protected
# private

class Character:
    def __init__(self, name):
        self.name = name  # public
        self._damage = 10  # protected
        self.__hp = 100  # private

    def func(self):
        var = self._damage
        var2 = self.__hp
        return var

    @property
    def damage(self):
        return self._damage


class Enemy(Character):

    def func(self):
        var = self._damage

        return var


char = Character('Jack')
print(char.name)
# char.name = 'Helen'
# print(char.name)
print(Enemy('Bob').damage)
print(char.__dict__)
print(char._Character__hp)
