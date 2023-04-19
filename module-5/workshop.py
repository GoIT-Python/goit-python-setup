# from re import search

# # 0504567813

# regexp = r"^((\+|\+3|\+38)?0?[\s]?\d+){10,13}"
# # regexp = r"^[\+]?[(]?[0-9]{1,3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

# phone_numbers = [
#     "0504567813",
#     "380(50)4567813",
#     "+380504567813",
#     "+380-50-4567813",
#     "+380 50 4567813",
#     "+380 (50) 4567813",
#     "+380 (50) 456 78 13",
#     "+380 (50) 456-7813",
#     "+380 (50) 456-78-13",
#     "+1 514 456 7813",
# ]

# for number in phone_numbers:
#     result = search(regexp, number)

#     if result is None:
#         print(f"Negative result: {number}")
#     else:
#         print(f"Positive result: {result.group()}")

bad_words = ["bad", "mat", "vodka"]

while True:
    user_input = input()

    for word in bad_words:
        user_input = user_input.replace(word, "*" * len(word))

    print(f"Me: {user_input}")
