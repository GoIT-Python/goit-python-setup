class Singleton:
    instance = None

    def __new__(cls, class_=None, *args, **kwargs):
        if not isinstance(class_.instance, class_):
            class_.instance = object.__new__(class_, *args, **kwargs)
        return class_.instance


class A(Singleton):
    pass


a = A()
print(a)
a1 = A()
print(a1)
