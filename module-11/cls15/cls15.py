class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.content = ' '

    def __repr__(self):
        return f'Cell: {self.x} {self.y} | {self.content} |'

    def __str__(self):
        return f'Cell: {self.x} {self.y} | {self.content} |'


class Map:

    def __init__(self):
        self.__x = 5
        self.__y = 5
        self.map = [[Cell(j, i) for i in range(self.__y)] for j in range(self.__x)]
        self.__current_x = 0
        self.__current_y = 0

    def __next__(self):

        if self.__current_x == self.__x:
            self.__current_x = 0
            self.__current_y += 1

            if self.__current_y == self.__y:
                self.__current_x = 0
                self.__current_y = 0
                raise StopIteration('Done')

        cell = self.map[self.__current_x][self.__current_y]
        cell.content = 'X'
        self.__current_x += 1
        return cell

    def __iter__(self):
        return self

    def __repr__(self):
        my_map = ''
        row = ' | '

        for cell in w_map:
            if self.__current_x < self.__x:
                row += cell.content + ' | '
            if self.__current_x == self.__x - 1:
                my_map += row + '\n'
                row = ' | '
        return my_map


w_map = Map()

print(w_map)
