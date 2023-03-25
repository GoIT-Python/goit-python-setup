def total(a=5, *numbers, **phone_book):
    print("a", a)
    # проход по всем элементам кортежа
    print("numbers: ", numbers)
    for item in numbers:
        print("item", item)

    # проход по всем элементам словаря
    print("phone_book: ", phone_book)
    for key, value in phone_book.items():
        print("key: ", key, "value: ", value)


print(total(10, 1, 2, 3, 7, 12, "x", j=4, Jack=1123, John=2231, Inge=1560))
