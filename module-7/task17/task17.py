data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]


def encode(data):
    if not data:
        return []
    counter = 0
    res = []
    for ind, i in enumerate(data):
        if not res:
            res.append(i)
            counter += 1
        elif i == res[-1]:
            counter += 1
        else:
            res.append(counter)
            res.extend(encode(data[ind:]))
            return res
    res.append(counter)
    print(res)
    return res


print(encode(data))
