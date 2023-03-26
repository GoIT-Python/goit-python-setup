def get_fullname(first_name, last_name, middle_name=None):
    if not middle_name:
        return f"{first_name + ' ' + last_name}"
    elif middle_name:
        return f"{first_name + ' '  +middle_name + ' ' + last_name}"


print(get_fullname("Petro", middle_name="Ivanovich", last_name="Zaliznyak"))
# print(get_fullname("Petro", "Zaliznyak"))

# Petro Ivanovich Zaliznyak
