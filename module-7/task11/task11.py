string = "Hello, World!"


# 1	. , ? ! :
# 2	A B C
# 3	D E F
# 4	G H I
# 5	J K L
# 6	M N O
# 7	P Q R S
# 8	T U V
# 9	W X Y Z
# 0	Пробел

dict = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "],
}


def sequence_buttons(string):
    res = ""
    for ch in string.upper():
        for key, value in dict.items():
            if not ch in value:
                continue
            if ch in value:
                res += key * (value.index(ch) + 1)

    print(res)
    return res

    # x = ch
    # y = btn

    # my_table = string.maketrans(x, y)

    # print(string.translate(my_table))
    # return string.translate(my_table)


sequence_buttons(string)

# '4433555555666110966677755531111'
