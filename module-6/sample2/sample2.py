output = "sample2.txt"
# text = "fnvdklfnknkbr\n"

file = open(output, "r")

# file.write(text)

text = file.read(1)
print(file.tell())
file.seek(6)
text = file.read()
file.seek(0)
text = file.read()


print(text)

file.close()
