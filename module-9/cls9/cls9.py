import functools


def simple_decorator(func):
    @functools.wraps(func)
    def simple_wrapper(*args, **kwargs):
        print("Before func")
        res = func(*args, **kwargs)
        print("After func")
        return res

    return simple_wrapper


def simple_decorator_2(func):
    @functools.wraps(func)
    def simple_wrapper(*args, **kwargs):
        print("Before func_2")
        res = func(*args, **kwargs)
        print("After func_2")
        return res

    return simple_wrapper


@simple_decorator
@simple_decorator_2
def mult(x, y):
    print("Mult")
    return x * y


result = mult(3, 7)
print(result)
