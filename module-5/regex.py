# import re

from re import search, findall, sub

# url_regexp = r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)"
# url = "http://www.google.com"

# result = re.search(
#     url_regexp,
#     url,
# )

# result = re.findall(
#     url_regexp,
#     url,
# )

# phone_number_regexp = r"^[\+]?[(]?[0-9]{3}[)]?[.]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# phone = "380 504567813"

# result = search(
#     phone_number_regexp,
#     phone,
# )

# regexp = r"^Hello"
# regexp = r"Hello$"
# regexp = r"H*"
# regexp = r"rl+"
# regexp = r"ll?"
# regexp = r"s{2,}"
# regexp = r"worl(ds)?"
# regexp = r"world(s|e)"
# regexp = r"world[se]"
# regexp = r"world\d"
# regexp = r"world\d*"
# regexp = r"world(\d|s)*"
# regexp = r"world(\w|s)*"
# regexp = r"world(\s|s)*"
# regexp = r"world."
# regexp = r"world\D"
# regexp = r"world[a-d]"
# regexp = r"world[0-3]"
# regexp = r"world[a-dA-D0-3s]"
# regexp = r"world[^a-dA-D0-3s]"
# regexp = r"\B\d"
regexp = r"\s"

str = "Hello worlds"

result = findall(regexp, str)

print(result)
