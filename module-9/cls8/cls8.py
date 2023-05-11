import functools


def simple_decorator(func):
    @functools.wraps(func)
    def simple_wrapper(*args, **kwargs):
        # print("Before func")
        res = func(*args, **kwargs)
        # print("After func")
        return res

    return simple_wrapper


@simple_decorator
def mult(x, y):
    return x * y


# result = mult(3, 7)
# print(result)
print(mult)
print(mult.__name__)
