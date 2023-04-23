def save_applicant_data(source, output):
    list = []
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
    with open(output, "w") as fh:
        for item in list:
            fh.write(item + "\n")
