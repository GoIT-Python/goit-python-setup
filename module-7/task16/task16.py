data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]


list = []


def decode(data):
    if not (bool(data)):
        return data
    for ch in data.pop(0) * data.pop(0):
        list.append(ch)
    decode(data)
    return list


res = decode(data)
print(res)
