def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper


@decorator
def sum(iterable, func=sum):
    print("Custom")
    return func(iterable)


result = sum([1, 2, 3, 4, 5])
print(result)
