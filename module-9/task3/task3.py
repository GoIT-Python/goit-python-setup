def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n):
        if n not in cache:
            value = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = value
        return cache[n]

    return fibonacci


caching_fibonacci()
