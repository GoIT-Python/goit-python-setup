source = "sample6.txt"

with open(source, "r+") as file:
    file.seek(5)
    file.write("\nasd\n")
