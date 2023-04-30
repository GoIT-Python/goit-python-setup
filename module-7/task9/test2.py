# Python program to print all
# sublist from a given list
from itertools import combinations

# data = [4, 6, 1, 3]


# function to generate all the sub lists
def sub_lists(l):
    # initializing empty list
    comb = []

    # Iterating till length of list
    for i in range(len(l) + 1):
        # Generating sub list
        comb += [list(j) for j in combinations(l, i)]
    # Returning list
    print(comb)
    return comb


# driver code
# Initial list
# l1 = [1, 2, 3]
l1 = [4, 6, 1, 3]

# Print initial list
print("Initial list is : " + str(l1))

# Calling function to generate all sub lists
print("All sub list is : " + str(sub_lists(l1)))
