def simple_decorator(func):
    def simple_wrapper():
        print("Before func")
        func()
        print("After func")

    return simple_wrapper


# def func():
#     print("Hello world")


@simple_decorator
def func():
    print("Hello world")


# decor = simple_decorator(func)
# decor()

func()  # func = simple_decorator(func)
