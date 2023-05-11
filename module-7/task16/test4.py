data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]


def decode(data):
    if not (bool(data)):
        return []
    else:
        return decode(data[0])


print(decode(data))


# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# factorial(5)    # 120
