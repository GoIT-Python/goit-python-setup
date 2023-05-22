class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f'str:({self.x}, {self.y})'

    def __repr__(self):
        return f'repr:({self.x}, {self.y})'


char_position = Position(1, 3)
print(char_position)
