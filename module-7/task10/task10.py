keys = ["name", "age", "email"]
values = ["Nick", "23", "nick@test.com"]


def make_request(keys, values):
    if not len(keys) == len(values):
        return {}
    dict = {}

    for i in range(len(keys)):
        dict[keys[i]] = values[i]

    print(dict)
    return dict


make_request(keys, values)

# Ожидалось, что функция make_request при получении параметров:
# (['name', 'age', 'email'], ['Nick', '23', 'nick@test.com'])
# вернет следующий список:
# {'name': 'Nick', 'age': '23', 'email': 'nick@test.com'}
