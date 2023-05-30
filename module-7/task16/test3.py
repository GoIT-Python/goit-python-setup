data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]


def decode(data):
    if not (bool(data)):
        return data
    else:
        res = [data.pop(0) * data.pop(0) for i in data]
        res.append(data.pop(0) * data.pop(0))
        return res


fin = decode(data)
print(fin)
