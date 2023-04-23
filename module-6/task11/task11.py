path = "task11.txt"


def get_credentials_users(path):
    list = []

    with open(path, "rb") as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            if not idx == len(lines) - 1:
                list.append(line.decode()[:-1])
            else:
                list.append(line.decode())

    return list


get_credentials_users(path)
