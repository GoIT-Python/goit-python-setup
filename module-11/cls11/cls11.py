class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Position):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        elif isinstance(other, list):
            return other

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __pow__(self, power, modulo=None):
        pass


char_position = Position(1, 1)
enemy_position = Position(3, 3)
print(char_position + enemy_position)
