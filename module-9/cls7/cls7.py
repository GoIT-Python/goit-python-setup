def simple_decorator(func):
    def simple_wrapper(*args, **kwargs):
        print("Before func")
        res = func(*args, **kwargs)
        print("After func")
        return res

    return simple_wrapper


@simple_decorator
def func(text):
    print(text)


# @route('google.com/v1/status')
# def func(text):
#     print(text)


@simple_decorator
def add(x, y):
    print(x + y)


@simple_decorator
def mult(x, y):
    return x * y


# func("Hello world")  # func = simple_decorator(func)

# add(2, 5)  # func = simple_decorator(func)

result = mult(3, 7)
print(result)
