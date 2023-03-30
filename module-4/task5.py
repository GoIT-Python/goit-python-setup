def lookup_key(data, value):
    result = list()
    for key, i in data.items():
        if i == value:
            result.append(key)
    return result


print(lookup_key({"key1": 1, "key2": 2, "key3": 3, "key4": 2}, 2))

# Функция lookup_key вернула неправильный список ключей: []. Должно быть lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2)==['key2', 'key4']
