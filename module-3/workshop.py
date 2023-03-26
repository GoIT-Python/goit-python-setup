def fnc(x):
    def add_ten():
        return x + 10

    return add_ten


first = fnc(5)
second = fnc(2)

print(first() + second())
