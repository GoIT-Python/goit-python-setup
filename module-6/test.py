text = "Alex Korp,3000"

# print(text[10:])

for idx, ch in enumerate(text):
    if ch == ",":
        res = text[(idx + 1) :]
        print(res)
