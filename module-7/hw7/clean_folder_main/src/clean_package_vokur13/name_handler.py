from re import sub
from transliterate.decorators import transliterate_function


@transliterate_function(language_code="uk", reversed=True)
def translit(text):
    return text


regex = r"[^a-zA-Z0-9]"


def normalize(text):
    return sub(regex, "_", translit(f"{text}"))
