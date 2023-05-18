class Record:

    def __init__(self, name):
        self.name = name


class Name:
    value = 'Boris'

    # def __str__(self):
    #     return self.value


record = Record(Name())
print(record.name)
print(record.name.value)
