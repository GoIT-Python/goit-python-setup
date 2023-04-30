source_file = "./source.txt"
output_file = "./output.txt"


def to_indexed(source_file, output_file):
    list = []
    res = ""
    with open(source_file, "r") as fh:
        lines = fh.readlines()
        for line in lines:
            list.append(line)
    i = 0
    for line in list:
        res += f"{i}" + ": " + line
        i += 1

    with open(output_file, "w") as fh:
        pass
        fh.write(res)


to_indexed(source_file, output_file)
