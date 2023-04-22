import re

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn "

spam_words = ["began", "Python"]


def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub(word, "*" * len(word), text, flags=re.IGNORECASE)
    return text


print(replace_spam_words(text, spam_words))


# Функция replace_spam_words возвращает неправильный результат: Guido van Rossum ***** working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn . Ожидалось, что при вызове функции replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']) будет получен следующий результат Guido van Rossum ***** working on ****** in the late 1980s, as a successor to the ABC programming ****** language, and first released ****** it in 1991 as ****** 0.9.0. ******
