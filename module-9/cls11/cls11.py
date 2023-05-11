def func(n):
    i = 0
    while i < n:
        print("Entry point")
        yield i
        print("After yield")
        i += 1


result = func(5)
# next(result)
# print("In between")
# next(result)

for item in result:
    print(item)
