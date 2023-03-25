# while True:
#     a = int(input("Enter value a: "))
#     operand = input("Enter operand: ")
#     b = int(input("Enter value b: "))

#     if operand == "+":
#         result = a + b
#     elif operand == "-":
#         result = a - b

#     print(result)

while True:
    value = input("Enter value: ")
    operator = str(input("Enter operator: "))
    print("value: ", value)
    print("operator: ", operator)
    try:
        operator == "+"
    except ValueError:
        print(f"Wrong operator")
    else:
        print("Else")

    # print(operator in value)
