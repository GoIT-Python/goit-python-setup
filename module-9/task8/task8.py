list_contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }
]


def get_emails(list_contacts):
    list = []
    for item in map(lambda item: item, list_contacts):
        list.append(item["email"])
    return list


get_emails(list_contacts)
