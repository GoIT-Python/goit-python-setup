def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result + 10

    print("After 2")

    return wrapper


@decorator
def func(x, y):
    return x + y


result = func(2, 5)
print(result)
