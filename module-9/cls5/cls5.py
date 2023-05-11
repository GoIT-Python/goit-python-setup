from math import cos

# x = int(input("X: "))
# y = int(input("Y: "))
# operator = input("Operator: ")

# if operator == "+":
#     print(x + y)
# elif operator == "-":
#     print(x - y)
# elif operator == "*":
#     print(x * y)
# elif operator == "/":
#     print(x / y)


# def handle_calculate(x, y, operator):
#     if operator == "+":
#         result = x + y
#     elif operator == "-":
#         result = x - y
#     elif operator == "*":
#         result = x * y
#     elif operator == "/":
#         result = x / y

#     return result


# print(handle_calculate(10, 4, "+"))


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


def div(x, y):
    return x / y


def pow(x, y):
    return x**y


# print(div(234, 465))

operations = {"+": add, "-": sub, "*": mul, "/": div, "**": pow, "cos": cos}

# print(operations["+"](3, 5))
# print(operations["**"](3, 5))


def operate(operator):
    return operations[operator]


handler = operate("/")
print(handler(3, 56))
print(operate("*")(4, 8))
print(operate("cos")(90))
