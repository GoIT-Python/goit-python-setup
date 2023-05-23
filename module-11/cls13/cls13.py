class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __and__(self, other):
        # &
        return 'ASD'

    def __or__(self, other):
        # |
        pass

    def __xor__(self, other):
        # ^
        pass


char_position = Position(1, 1)
enemy_position = Position(3, 1)

print(char_position == enemy_position)
print(char_position != enemy_position)
print(char_position & enemy_position)
