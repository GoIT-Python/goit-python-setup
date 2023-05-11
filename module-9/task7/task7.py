list_name = ["dan", "jane", "steve", "mike"]


def normal_name(list_name):
    list = []
    for name in map(lambda name: name.capitalize(), list_name):
        list.append(name)
    return list


print(normal_name(list_name))
print(list_name)
