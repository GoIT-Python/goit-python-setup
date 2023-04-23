# source = "source.txt"
source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
output = "output.txt"


def save_applicant_data(source, output):
    list = []
    new_list = []
    for item in source:
        result = "".join(
            "{},{},{},{},{}".format(
                item.get("name"),
                item.get("specialty"),
                item.get("math"),
                item.get("lang"),
                item.get("eng"),
            )
        )

        list.append(result)

    for item in list:
        if not item == list[-1]:
            item = item + "\n"
        else:
            item = item

        new_list.append(item)

    with open(output, "w") as fh:
        fh.writelines(new_list)


save_applicant_data(source, output)
