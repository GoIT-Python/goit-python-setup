class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self.x, self.y

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self.x, self.y


position1 = Position(1, 10)
position2 = Position(10, 10)

position3 = position1 + position2
position4 = position2 - position1

print(position3)
print(position4)
