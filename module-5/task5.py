list_phones = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "    +81(050)123-32-34",
    "    +65(050)123-32-34",
    "    +886(050)123-32-34",
]


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    country_code = [
        ("Japan", "+81"),
        ("Singapore", "+65"),
        ("Taiwan", "+886"),
        ("Ukraine", "380"),
    ]

    phone_dict = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": [],
    }

    for phone in list_phones:
        sanitize_phone = sanitize_phone_number(phone)
        if sanitize_phone.startswith(country_code[0][1][1::]):
            phone_dict["JP"].append(sanitize_phone)
        elif sanitize_phone.startswith(country_code[1][1][1::]):
            phone_dict["SG"].append(sanitize_phone)
        elif sanitize_phone.startswith(country_code[2][1][1::]):
            phone_dict["TW"].append(sanitize_phone)
        else:
            phone_dict["UA"].append(sanitize_phone)

    return phone_dict


print(get_phone_numbers_for_countries(list_phones))
