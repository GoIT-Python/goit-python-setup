# comprehensions

my_list=[]
# for i in range(10):
#     my_list.append(i*10)

for i in range(10):
    if i% 2:
        my_list.append(i * 10)
print(my_list)

# my_list_comp=[i*10 for i in range(10)]
# [compr(i) for i in iterable if condition]
my_list_comp=[i*10 for i in range(10) if i% 2]
print(my_list_comp)






