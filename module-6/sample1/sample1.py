text = "sample1.txt"

file = open(text, "r")
# text = file.read(2)
# print(text)
# text = file.read(2)
# print(text)
# text = file.read(2)

# while True:
#     text = file.read(5)
#     if not text:
#         break
#     print(text)

# text = file.readline()
# text = file.readlines()

for line in file:
    print(line)

# print(text)

file.close()
