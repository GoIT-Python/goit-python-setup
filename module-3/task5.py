def get_fullname(
    first_name,
    middle_name="",
    last_name="",
):
    if not middle_name:
        return f"{first_name, last_name}"
    elif middle_name:
        return f"{first_name, middle_name, last_name}"


print(get_fullname(first_name="Petro", last_name="Zaliznyak"))

# Petro Ivanovich Zaliznyak
