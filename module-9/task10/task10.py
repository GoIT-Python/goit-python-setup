contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }
]


def get_favorites(contacts):
    list = []
    for i in filter(lambda i: i, contacts):
        if i["favorite"]:
            list.append(i)
    print(list)
    return list


get_favorites(contacts)
