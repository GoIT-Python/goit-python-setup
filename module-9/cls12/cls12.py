def my_range(x, y):
    while x < y:
        yield x
        x += 1


# for i in my_range(0, 10):
#     print(i)


a = (i for i in [1, 2, 3])

print(next(a))
print(next(a))
print(next(a))
