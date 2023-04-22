phone = "38050 111 22 11   "
char_to_delete = ["(", "-", ")", "+", " "]

for char in char_to_delete:
    pass
    # print(char in phone)


def sanitize_phone_number(phone):
    result = ""
    strip = phone.strip()
    for char in strip:
        if char in char_to_delete:
            continue
        else:
            result += char
    return result


print(sanitize_phone_number(phone))

#  "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
