class Character:
    def __init__(self, name):
        self.name = name  # public
        self._damage = 10  # protected
        self.__hp = 100  # private

    def public(self):
        pass

    def _protected(self):
        pass

    def __private(self):
        pass
