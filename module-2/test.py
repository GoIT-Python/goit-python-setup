result = None
operand = None
operator = None
wait_for_number = True

while True:
    if wait_for_number:
        operand = input("Enter operand: ")
        try:
            operand = int(operand)
        except ValueError:
            print(f"operand {operand} is not a number, try again")
            continue
        else:
            if not operator:
                result = operand

            elif "+" in operator:
                result += operand

            elif "-" in operator:
                result -= operand

            elif "*" in operator:
                result *= operand

            elif "/" in operator:
                result /= operand

            wait_for_number = False

    elif not wait_for_number:
        operator = input("Enter operator: ")

        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            print("it is ok!")
            print("operator:", operator)
            wait_for_number = True
        elif operator == "=":
            result = float(result)
            break
        else:
            print(f"{operator} is not: '+' or '-' or '/' or '*', try again")
            continue

print("result:", result)


# Первая: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "="], результат 18.0

# Вторая: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0
