path = "task5.txt"


def get_cats_info(path):
    list = []
    cats_list = []
    with open(path, "r") as fh:
        while True:
            line = fh.readline()
            if not line:
                break
            list.append(line.strip())
            for item in list:
                cat = item.split(",")
            cats_list.append({"id": cat[0], "name": cat[1], "age": cat[2]})

    return cats_list


get_cats_info(path)
