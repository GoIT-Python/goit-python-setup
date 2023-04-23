path = "task3.txt"


def read_employees_from_file(path):
    list = []
    fh = open(path, "r")

    while True:
        line = fh.readline()
        if not line:
            break
        list.append(line.strip())

    fh.close()
    return list


read_employees_from_file(path)


# ['Robert Stivenson, 28', 'Alex Denver, 30', 'Drake Mikelsson, 19']
#  ['Alexandr Popov,28', 'Larisa Host,31', 'Pavel Durov,29']
