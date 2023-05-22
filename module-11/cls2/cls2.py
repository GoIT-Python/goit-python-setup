my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2}


# print(my_list[0])
# print(my_dict['a'])

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords_list = [self.x, self.y]
        self.coords_dict = {'x': self.x, 'y': self.y}

    def __setitem__(self, key, value):
        # if key in (0, 1):
        #     self.coords[key] = value
        if isinstance(key, str):
            self.coords_dict[key] = value
        elif isinstance(key, int):
            self.coords_list[key] = value

        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            pass
            # raise ValueError('Index could be either 0 or 1')

        # return value
        # return self.coords

    def __getitem__(self, key):
        print(f'You are trying to get an element with key {key}')
        return self.coords_list[key]


char_position = Position(1, 3)
char_position[0] = 2
char_position[1] = 7
print(char_position[0])
print(char_position[1])
char_position['a'] = 5
char_position['b'] = 12
print(char_position.coords_dict)
