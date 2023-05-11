list_payment = [100, -3, 400, 35, -100]


def positive_values(list_payment):
    list = []
    for i in filter(lambda x: x > 0, list_payment):
        list.append(i)
    print(list)
    return list


positive_values(list_payment)
