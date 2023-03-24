message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if ch != " ":
        pos = ord(ch) - ord("a")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("a"))
        encoded_message += new_char
    elif ch == " ":
        encoded_message += " "

print(encoded_message)

# 'Hello my little friends!' -> 'Spwwz xj wteewp qctpyod!' offset=37

# "Hello world!", offset = 7
