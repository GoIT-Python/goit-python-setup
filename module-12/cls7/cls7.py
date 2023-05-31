from copy import copy, deepcopy

a = [1, 2, 3]
b = [a, 4, 5]
c = b
print(c)

b[0][0] = 7
print(b)

c = copy(b)
print(b)
print(c)

b[0][0] = 9
print(b)
print(c)
print(id(b[0]))
print(id(c[0]))

c = deepcopy(b)
print(b)
print(c)
print(id(b))
print(id(c))
print(id(b[0]))
print(id(c[0]))
