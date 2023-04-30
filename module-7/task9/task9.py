# data = [1, 2, 3]
data = [4, 6, 1, 3]


def all_sub_lists(data):
    if not data:
        return [[]]

    list = [[]]

    start_idx = 0

    for i in data:
        res = []
        res.append(i)
        list.append(res)

    if len(data) > 1:
        for i in range(len(data) - 1):
            list.append(data[start_idx : (i + 2)])
            start_idx += 1

    if len(data) > 2:
        start_idx = 0
        res = []
        for n in range(3, len(data)):
            for i in range(len(data) - 1):
                res = data[start_idx : (i + n)]
                if not len(res) < n:
                    list.append(res)
                start_idx += 1
            n += 1

    list.append(data)

    print(list)
    return list


all_sub_lists(data)

# [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
# [[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]
