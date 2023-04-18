articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result_list = []

    for dict in articles_dict:
        for k, _ in dict.items():
            if not k == "year":
                if (dict[k].casefold()).find(key.casefold()) > 0:
                    result_list.append(dict)
    return result_list


# find_articles("Ocean", False)
print(find_articles("Ocean"))

# find_articles('Ocean') == [{'title': 'Endless ocean waters.', 'author': 'Jhon Stark', 'year': 2019}, {'title': 'Oceans of other planets are full of silver', 'author': 'Artur Clark', 'year': 2020}, {'title': 'An ocean that cannot be crossed.', 'author': 'Silver Name', 'year': 2021}, {'title': 'The ocean that you love.', 'author': 'Golden Gun', 'year': 2021}]
