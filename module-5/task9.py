def formatted_numbers():
    numbers_list = []

    numbers_list.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))

    for i in range(16):
        shex = hex(i)[2::]
        sbin = bin(i)[2::]
        numbers_list.append("|{:<10}|{:^10}|{:>10}|".format(int(i), shex, sbin))

    return numbers_list


for el in formatted_numbers():
    print(el)

# | decimal  |   hex    |  binary  |
# |0         |    0     |         0|
# |1         |    1     |         1|
# |2         |    2     |        10|
# |3         |    3     |        11|
# |4         |    4     |       100|
# |5         |    5     |       101|
# |6         |    6     |       110|
# |7         |    7     |       111|
# |8         |    8     |      1000|
# |9         |    9     |      1001|
# |10        |    a     |      1010|
# |11        |    b     |      1011|
# |12        |    c     |      1100|
# |13        |    d     |      1101|
# |14        |    e     |      1110|
# |15        |    f     |      1111|
