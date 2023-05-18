class A:
    def __init__(self):
        print('I am A')


class B(A):
    def __init__(self):
        super().__init__()
        print('I am B')


a = A()
a
b = B()
b
