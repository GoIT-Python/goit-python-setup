def is_valid_password(password):
    if not len(password) == 8:
        return False

    upper = []
    lower = []
    numeric = []

    for i in password:
        if not i.isupper():
            continue
        upper.append(i)
    if not upper:
        return False

    for i in password:
        if not i.islower():
            continue
        lower.append(i)
    if not lower:
        return False

    for i in password:
        if not i.isnumeric():
            continue
        numeric.append(i)
    if not numeric:
        return False

    return True


print(is_valid_password("p^AS?uX("))
