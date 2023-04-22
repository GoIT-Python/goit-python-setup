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


def find_articles(word, letter_case=False):
    result_list = []

    for article in articles_dict:
        for key, _ in article.items():
            if not type(article[key]) == int:
                if not letter_case:
                    if not article[key].casefold().find(word.casefold()) == -1:
                        result_list.append(article)
                else:
                    if not article[key].find(word) == -1:
                        result_list.append(article)

    return result_list


print(find_articles("Ocean"))

# find_articles('Ocean') == [{'title': 'Endless ocean waters.', 'author': 'Jhon Stark', 'year': 2019}, {'title': 'Oceans of other planets are full of silver', 'author': 'Artur Clark', 'year': 2020}, {'title': 'An ocean that cannot be crossed.', 'author': 'Silver Name', 'year': 2021}, {'title': 'The ocean that you love.', 'author': 'Golden Gun', 'year': 2021}]
