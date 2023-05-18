class A:
    field = None

    def method(self):
        pass


var = A().__dict__
print(var)

var2 = A.__dict__
print(var2)
