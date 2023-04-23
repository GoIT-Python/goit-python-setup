path = "task10.txt"
users_info = {"andry": "uyro18890D", "steve": "oppjM13LL9e"}


def save_credentials_users(path, users_info):
    list = []
    for key, value in users_info.items():
        str = "".join("{}:{}\n".format(key, value))
        list.append(str)

    with open(path, "wb") as file:
        for item in list:
            file.write(item.encode())


save_credentials_users(path, users_info)
