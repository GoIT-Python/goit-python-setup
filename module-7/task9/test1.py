# Python program to print all
# sublist from a given list


# function to generate all the sub lists
def all_sub_lists(data):
    lists = [[]]
    for i in range(len(data) + 1):
        for j in range(i):
            lists.append(data[j:i])
    return lists


# driver code
# l1 = [1, 2, 3]
l1 = [4, 6, 1, 3]
print(all_sub_lists(l1))

# [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]

# Ожидалось, что функция all_sub_lists при получении параметров:
# '[4, 6, 1, 3]'
# вернет следующий список:
# [[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]
