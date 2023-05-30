data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]


def decode(data):
    if not (bool(data)):
        return data
    else:

        res = ([data.pop(0) * data.pop(0) for i in data])
        print('res', res)
        res.append(decode(data[-2:]))


decode(data)
# fin = decode(data)
# print(fin)
