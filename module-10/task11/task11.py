from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for ch in self.data:
            if ch.isdigit():
                count += 1
        return count
