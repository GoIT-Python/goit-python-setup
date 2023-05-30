import json

contacts_list = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Cyrus Jackson",
        "email": "nibh@semsempererat.com",
        "phone": "(501) 472-5218",
        "favorite": True,
    }
]

file_name = 'data.json'


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as fh:
        json.dump({'contacts': contacts}, fh)


def read_contacts_from_file(filename):
    with open(filename, 'r') as fh:
        unpacked = json.load(fh)
        return unpacked['contacts']


write_contacts_to_file(file_name, contacts_list)
print(read_contacts_from_file(file_name))
