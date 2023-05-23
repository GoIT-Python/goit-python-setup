class Iterator:
    MAX_VALUE = 10

    def __init__(self):
        self.start = 7

    def __next__(self):
        if self.start < self.MAX_VALUE:
            self.start += 1
            print(f'Hy, I am iteration number {self.start}')
            return self.start
        raise StopIteration


class MyIterator:
    def __iter__(self):
        return Iterator()


my_iterable = MyIterator()

for i in my_iterable:
    print(i)
