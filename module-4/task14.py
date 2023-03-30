import sys


def parse_args():
    result = ""

    for arg in sys.argv[1:]:
        result += arg + " "

    return result.strip()


print(parse_args())
