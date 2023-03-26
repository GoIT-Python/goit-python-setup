# def print_hello():
#     calculate()
#     print("Hello world!")


# def calculate():
#     x = 3
#     y = 5

#     def inner_func():
#         nonlocal x
#         print(x)
#         x = 10
#         print(x)

#     inner_func()

#     return x + y


# print(calculate())

#  flexible number of arguments


def calculate(*args, a=12, **kwargs):
    # for arg in args:
    #     print(arg)
    print(args)
    print(kwargs)
    print(a)
    # return args


result = calculate(1, 2, 3, 5, 8, 9, a=5, b=10, c=4)
# print(result)
