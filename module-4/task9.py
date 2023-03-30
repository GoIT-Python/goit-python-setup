def is_valid_pin_codes(pin_codes):
    if not pin_codes:
        return False

    for i in pin_codes:
        if (
            not type(i) == str
            or not len(i) == 4
            or not sorted(pin_codes) == sorted(list(set(pin_codes)))
        ):
            return False
        for j in i:
            if not j.isnumeric():
                return False

    return True


print(is_valid_pin_codes(["1101", "9034", "0011"]))
