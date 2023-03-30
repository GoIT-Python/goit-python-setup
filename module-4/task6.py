def split_list(grade):
    lower = list()
    upper = list()

    if len(grade):
        avg = sum(grade) / len(grade)

    for i in grade:
        if not i > avg:
            lower.append(i)
        else:
            upper.append(i)
    return (lower, upper)


print(split_list([1, 2, 3, 4, 5]))
