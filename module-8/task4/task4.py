from random import randrange

min = 1
max = 49
quantity = 6


def get_numbers_ticket(min, max, quantity):
    if not min > 0:
        return []
    elif not max < 1001:
        return []
    elif not min < quantity < max:
        return []

    numbers = []
    i = min
    while i <= quantity:
        number = randrange(min, max + 1)
        if not number in numbers:
            numbers.append(number)
            i += 1
        else:
            continue
    res = sorted(numbers)
    print(res)
    return res


get_numbers_ticket(min, max, quantity)
