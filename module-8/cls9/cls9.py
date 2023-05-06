from collections import deque

d = deque()
d.append("last")
d.appendleft("first")
d.insert(1, "middle")
print(d)  # deque(['first', 'middle', 'last'])
