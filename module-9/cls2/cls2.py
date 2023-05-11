def func_1(arg):
    arg()


def func_2():
    print("Hello")


# arg = func_2
x = func_2
func_1(x)
