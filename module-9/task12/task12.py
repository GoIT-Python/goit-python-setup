from functools import reduce

payment = [1, -3, 4]


def amount_payment(payment):
    list = []
    for i in filter(lambda x: x > 0, payment):
        list.append(i)
    total = reduce((lambda x, y: x + y), list)
    print(total)
    return total


amount_payment(payment)
