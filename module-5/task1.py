def real_len(text):
    len = 0
    for i in text:
        if i in ["\n", "\f", "\r", "\t", "\v"]:
            continue
        else:
            len += 1
    return len


print(real_len("Alex\nKdfe23\t\f\v.\r"))

print(real_len("Al\nKdfe23\t\v.\r"))
