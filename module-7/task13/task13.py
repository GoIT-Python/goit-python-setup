path = "info.txt"
profession = "courier"


def get_employees_by_profession(path, profession):
    list = []
    with open(path, "r") as fh:
        lines = fh.readlines()
        for line in lines:
            if not line.find(profession) < 0:
                list.append(line[:-1])
    names = " ".join(list)
    return names.replace((" " + profession), "")


get_employees_by_profession(path, profession)
