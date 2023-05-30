import csv

list_ = [
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

data = 'data.csv'


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        fields_names = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter(fh, fieldnames=fields_names)
        writer.writeheader()
        for item in contacts:
            writer.writerow(
                {'name': item['name'], 'email': item['email'], 'phone': item['phone'], 'favorite': item['favorite']})


def read_contacts_from_file(filename):
    unpack = []
    with open(filename, 'r', newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            unpack.append(
                {'name': row['name'], 'email': row['email'], 'phone': row['phone'],
                 'favorite': True if row['favorite'] == 'True' else False})
    print(unpack)
    return unpack


write_contacts_to_file(data, list_)
read_contacts_from_file(data)
