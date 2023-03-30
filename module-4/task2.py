data = [3, 7, 9, 4, 1]


def prepare_data(data):
    max_i = data[0]
    min_i = data[0]

    for i in data:
        if i > max_i:
            max_i = i
    data.remove(max_i)

    for i in data:
        if i < min_i:
            min_i = i
    data.remove(min_i)

    data_sorted = sorted(data)

    return data_sorted


print(prepare_data(data))
