import pickle


class Reader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name)
        self.a = 123

    def read(self):
        return self.file.read()

    def __getstate__(self):
        attrs = self.__dict__.copy()
        attrs['file'] = None
        return attrs

    def __setstate__(self, state):
        self.__dict__ = state
        # self.__dict__['file'] = open(self.file_name) // ==
        self.file = open(self.file_name)


reader = Reader('data.csv')
serialized = pickle.dumps(reader)
print(serialized)

unpacked = pickle.loads(serialized)
print(unpacked.file)
