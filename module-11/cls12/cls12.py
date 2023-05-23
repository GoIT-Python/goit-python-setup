class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        # return self.x != other.x and self.y != other.y
        return not self.__eq__(other)

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass


char_position = Position(1, 1)
enemy_position = Position(3, 1)

print(char_position == enemy_position)
print(char_position != enemy_position)
