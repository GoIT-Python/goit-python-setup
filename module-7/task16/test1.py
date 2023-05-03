data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]


def decode(data):
    list = []
    i = 0
    while True:
        for ch in data[i] * data[i + 1]:
            list.append(ch)
        if i >= len(data) - 2:
            break
        i += 2

    print(list)
    return list


decode(data)
