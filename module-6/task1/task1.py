path = "task1.txt"


def total_salary(path):
    result = 0
    fh = open(path, "r")
    while True:
        line = fh.readline()
        if not line:
            break
        for idx, ch in enumerate(line):
            if ch == ",":
                result += float(line[(idx + 1) :])
    fh.close()
    return result


print(total_salary(path))
