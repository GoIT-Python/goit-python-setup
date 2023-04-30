def generateSublists(lst):
    # Base case
    if len(lst) == 0:
        return [[]]

    # Recursive case
    sublists = []
    first_element = lst[0]
    rest_list = lst[1:]
    sublists_of_rest = generateSublists(rest_list)
    # Generate sublists including first element
    for sublist in sublists_of_rest:
        sublists.append([first_element] + sublist)
    # Generate sublists excluding first element
    sublists.extend(sublists_of_rest)

    return sublists


# Driver code
l1 = [4, 6, 1, 3]
print(generateSublists(l1))
