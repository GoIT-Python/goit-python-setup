# closures


def multiply(x):
    def inner(y):
        def func(z):
            return x * y * z

        return func

    return inner


multiply_10 = multiply(10)
# multiply_3 = multiply(3)
# multiply_5 = multiply(5)

# multiply_10_3 = multiply_10(3)

# print(multiply_10)
print(multiply(10)(3)(4))
# print(multiply_10_3)
# print(multiply_10_3(2))

# print(multiply_3(7))
# print(multiply_5(7))
