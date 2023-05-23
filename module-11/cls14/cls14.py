class str(str):

    def __add__(self, other):
        return 1

    def __eq__(self, other):
        if isinstance(other, int):
            return super().__eq__(other.__str__())


# a = str('a')
# b = str('b')
#
# print(type(a))
# print(type(b))
#
# print(a + b)

print(str('1') == 1)
