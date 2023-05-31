import pickle


class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age


char = Character('Nina', 23)

# serialized = pickle.dumps(char)
# print(serialized)
#
# unpacked = pickle.loads(serialized)
# print(unpacked.name)

with open('data.bin', 'wb') as fh:
    pickle.dump(char, fh)

with open('data.bin', 'rb') as fh:
    unpacked = pickle.load(fh)

print(unpacked.name)
