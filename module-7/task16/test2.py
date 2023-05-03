data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

# def parse_folder(path):
#     for item in path.iterdir():
#         if item.is_dir():
#             parse_folder(item)
#         else:
#             print(f"This is file: {item}")

# def flatten(data):
#     if not (bool(data)):
#         return data

#     if isinstance(data[0], list):
#         return flatten(*data[:1]) + flatten(data[1:])

#     return data[:1] + flatten(data[1:])


def decode(data):
    if not (bool(data)):
        return data
    res = []
    res.append(data.pop(-1))
    res.append(data.pop(-1))
    decode(data)
    print(res)


decode(data)
