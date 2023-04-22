grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    i = 0
    mark = None
    students_list = []
    for name, value in students.items():
        for key, grade in grades.items():
            if key == students[name]:
                mark = grade
                i += 1
                students_list.append(
                    "{:>4}|{:<10}|{:^5}|{:^5}".format(i, name, value, mark)
                )
    return students_list


for el in formatted_grades(students):
    print(el)
