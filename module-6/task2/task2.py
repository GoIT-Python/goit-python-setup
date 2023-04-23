list = [["Robert Stivenson,28", "Alex Denver,30"], ["Drake Mikelsson,19"]]
path = "task2.txt"


def write_employees_to_file(employee_list, path):
    fh = open(path, "w")
    for div in employee_list:
        for item in div:
            fh.write(item + "\n")
    fh.close()


write_employees_to_file(list, path)

# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19
