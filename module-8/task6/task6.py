from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sum = 0
    for number in number_list:
        sum += Decimal(number)
    print(sum / len(number_list))
    return sum / len(number_list)


decimal_average([3, 5, 77, 23, 0.57], 6)  # вернет 21.714
decimal_average([31, 55, 177, 2300, 1.57], 9)  # вернет 512.91400
