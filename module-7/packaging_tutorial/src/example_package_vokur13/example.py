import sys
from pathlib import Path


def add_one():
    number = Path(sys.argv[1])
    return number + 1


# def hello():
#     print("Hello, World!")
