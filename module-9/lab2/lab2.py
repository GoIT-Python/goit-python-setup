def mul(i):
    return i * 2


# my_list = [1, 2, 3, 4, 5]
list_1 = [1, 2, 3, 4, 5]
list_2 = ["a", "b", "c", "d", "e"]

result = []
# for i in my_list:
#     element = mul(i)
#     result.append(element)

# result = list(map(mul, my_list))
# result = list(map(lambda i: i * 2, my_list))
# result = list(map(lambda i: i, {"a": 1, "b": 2}.items()))
# [mul(i) for i in my_list] - generator
# (mul(i) for i in my_list) - list expression

for n in map(lambda x, y: f"{y}: {x}", list_1, list_2):
    print(n)

# print(result)
