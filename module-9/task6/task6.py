import re

string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."

regex = r"\d+"


def generator_numbers(string):
    list = string.split(" ")
    for item in list:
        result = re.search(regex, item)
        if result:
            yield result.group()


def sum_profit(string):
    amount = 0
    for i in generator_numbers(string):
        amount += int(i)
    print(amount)
    return amount


sum_profit(string)
# generator_numbers(string)
