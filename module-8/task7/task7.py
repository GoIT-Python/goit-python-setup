import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

# cats = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
cats = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]


def convert_list(cats):
    cats_list = []
    for cat in cats:
        if bool(isinstance(cat, tuple)):
            cats_list.append(
                {"nickname": cat.nickname, "age": cat.age, "owner": cat.owner}
            )
        elif bool(isinstance(cat, dict)):
            cats_list.append(Cat(cat["nickname"], cat["age"], cat["owner"]))
    print(cats_list)
    return cats_list


convert_list(cats)
