class A:
    pass
    # def hello(self):
    #     print('hello A')


class B(A):
    pass
    # def hello(self):
    #     print('hello B')


class C:
    def hello(self):
        print('hello C')


class D(B, C):
    pass


D().hello()
