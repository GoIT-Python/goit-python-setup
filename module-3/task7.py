def first(size, *args):
    return size + len(args)


def second(size, **kwargs):
    return size + len(kwargs)


# print(first(5, "first", "second", "third"))

# print(first(1, "Alex", "Boris"))

print(second(3, comment_one="first", comment_two="second", comment_third="third"))

print(second(10, comment_one="Alex", comment_two="Boris"))
