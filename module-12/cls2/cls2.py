import pickle

a = (1, 2, 3)

with open('test.dat', 'wb') as fh:
    pickle.dump(a, fh)

with open('test.dat', 'rb') as fh:
    b = pickle.load(fh)

print(b)
