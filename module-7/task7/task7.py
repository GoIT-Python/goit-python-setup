# list_data = [[1, 2, 3], [3, 4], [5, 6]]
list_data = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]


def data_preparation(list_data):
    res = []
    for item in list_data:
        if not len(item) <= 2:
            item.sort()
            item = item[1:-1]

        res.extend(item)
        res.sort(reverse=True)

    print(res)
    return res


data_preparation(list_data)

# [6, 5, 4, 3, 2]

# Ожидалось, что функция data_preparation при получении параметров:
# ([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]])
# вернет следующий список:
# [6, 5, 3, 2, 2, 1]
