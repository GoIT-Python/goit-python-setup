from re import sub

text = """Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.

The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.

This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.

For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth."""

regexp = r"[^a-zA-Z0-9 ]"

normalized = text.lower()

normalized = sub(regexp, "", normalized)

words_list = normalized.split()

unique_words_list = set(words_list)

num_words = len(words_list)

num_inique = len(unique_words_list)

words_quantity = {}

for word in unique_words_list:
    words_quantity[word] = normalized.count(word)

words_quantity_list = list(words_quantity.items())


def sort_by_quantity(element):
    print(element.sort())
    # return element[1]


sort_by_quantity(words_quantity_list)


# result = words_quantity_list.sort(key=sort_by_quantity, reverse=True)

# print(result)
