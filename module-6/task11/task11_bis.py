path = "task11.txt"


def get_credentials_users(path):
    list = []
    with open(path, "rb") as file:
        lines = file.readlines()
        for line in lines:
            list.append(line.decode()[:-1])

    print(list)
    return list


get_credentials_users(path)
