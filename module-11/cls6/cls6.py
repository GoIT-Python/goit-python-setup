class Iterator:
    MAX_VALUE = 12

    def __init__(self):
        self.value = 0

    def __next__(self):
        if self.value >= self.MAX_VALUE:
            raise StopIteration
        self.value += 1
        print(f'Hy, I am iteration number {self.value}')
        return self.value

    def __iter__(self):
        return self


iterator = Iterator()

for i in iterator:
    print(i)
