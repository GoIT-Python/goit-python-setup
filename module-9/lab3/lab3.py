# for i in range(10):
#     if i % 2:
#         print(i)


def func(text):
    if text in ("bad", "mad", "vodka", "beer"):
        return False
    return True


bad_words = ("bad", "mad", "vodka", "beer")

# result = list(filter(lambda i: i % 2, range(10)))
# result = list(filter(func, ["apple", "vodka", "potato", "beer"]))
result = list(
    filter(lambda text: not text in bad_words, ["apple", "vodka", "potato", "beer"])
)
print(result)
