from random import randint


def get_random_password():
    password = ""

    while True:
        password += chr(randint(40, 126))
        if not len(password) < 8:
            break

    return password


print(get_random_password())

# password = input("Password: ")
# if len(password) > 12 or len(password) < 6:
#     print("The password must be between 6 and 12 characters long.")
