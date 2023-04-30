import re

# s = "2+ 34 - 5 * 3"
s = "(2+ 3) *4 - 5 * 3"

regex = r"\d+|\W"


def token_parser(s):
    list = []
    result = re.findall(regex, s)

    for item in result:
        if not item == " ":
            list.append(item)

    print(list)
    return list


token_parser(s)

# ['2', '+', '34', '-', '5', '*', '3']
# ['(', '2', '+', '3', ')', '*', '4', '-', '5', '*', '3']
