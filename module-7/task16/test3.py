data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]


def decode(data):
    if not (bool(data)):
        return data
    list = []
    for ch in data.pop(-1) * data.pop(-1):
        list.append(ch)
        decode(data)
    print(list)


decode(data)
