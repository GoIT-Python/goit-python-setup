def get_grade(key):
    ECTS = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
    return ECTS.get(key)


print(get_grade("F"))


def get_description(key):
    ECTS = {
        "F": "Unsatisfactorily",
        "FX": "Unsatisfactorily",
        "E": "Enough",
        "D": "Satisfactorily",
        "C": "Good",
        "B": "Very good",
        "A": "Perfectly",
    }
    return ECTS.get(key)


print(get_description("G"))
