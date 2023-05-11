def func_1(arg):
    return arg


def func_2():
    print("Hello")


x = func_2
a = func_1(x)
a()
