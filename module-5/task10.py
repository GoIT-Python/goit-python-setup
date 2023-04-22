import re


def find_word(text, word):
    result_dict = {}
    result = re.search(word, text)
    if not result:
        result_dict.update(
            {
                "result": False,
                "first_index": None,
                "last_index": None,
                "search_string": word,
                "string": text,
            }
        )
    else:
        result_dict.update(
            {
                "result": True,
                "first_index": result.span()[0],
                "last_index": result.span()[1],
                "search_string": word,
                "string": text,
            }
        )
    return result_dict


print(
    find_word(
        "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
        "Python",
    )
)

# {
#     'result': True,
#     'first_index': 34,
#     'last_index': 40,
#     'search_string': 'Python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }

# {
#     'result': False,
#     'first_index': None,
#     'last_index': None,
#     'search_string': 'python',
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# }
