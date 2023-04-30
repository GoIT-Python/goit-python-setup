import re

regex = r"[^.!?]+[.!?]?"

text = "hello world! awesome? yes"


def capital_text(s):
    res = re.findall(regex, s)
    list = []
    for item in res:
        list.append(item.strip().capitalize())
    new = " ".join(list)
    print(new)

    return new


capital_text(text)

# 'Hello world! Awesome? Yes'
