def is_spam_words(text, spam_words, space_around=False):
    for word in spam_words:
        if not space_around:
            return not text.casefold().find(word.casefold()) == -1
        else:
            for sub in text.split():
                if not sub.casefold().find(word.casefold()) == -1:
                    if sub.casefold().strip().find(word.casefold()) > 0:
                        return text.casefold().find(word.casefold()) == -1
                    elif sub.casefold().strip().find(word.casefold()) == 0:
                        if sub.casefold().strip().endswith("."):
                            return len(sub.casefold().strip()[0:-1]) == len(
                                word.casefold()
                            )
                        else:
                            return len(sub.casefold().strip()) == len(word.casefold())


print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True
