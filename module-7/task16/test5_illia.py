data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]


def decode(data):
    if data:
        if len(data) == 2:
            res = []
            for i in range(data[1]):
                res.append(data[0])
            return res
        else:
            return decode(data[:2]) + decode(data[2:])
    else:
        return []


print(decode(data))
