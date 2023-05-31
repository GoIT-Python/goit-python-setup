import pickle

a = (1, 2, 3)

serialized = pickle.dumps(a)
print(serialized)

unpacked = pickle.loads(serialized)
print(unpacked)

print(a == unpacked)
print(a is unpacked)
print(id(a))
print(id(unpacked))
