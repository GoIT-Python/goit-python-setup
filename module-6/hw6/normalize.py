from re import sub
from transliterate import get_translit_function

translit_uk = get_translit_function("uk")

regex = r"[^a-zA-Z0-9]"

# text = "Lorem ipsum dolor sit amet"
# text = "Lорем іпсум долор5 сіт аме*"


def normalize(text):
    return sub(regex, "_", translit_uk(f"{text}", reversed=True))


# print(normalize(text))
