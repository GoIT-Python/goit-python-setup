text = "steve:oppjM13LL9e\n"
str = ""


for ch in text:
    if not ch == "\n":
        str += ch
    else:
        continue

print(str)
