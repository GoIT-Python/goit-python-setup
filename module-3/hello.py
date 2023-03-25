import sys


def say_hello(name):
    print(f"Hello {name}")


def main():
    print("You imported hello.py")
    say_hello("user")


for arg in sys.argv:
    print("arg:", arg)
if __name__ == "__main__":
    main()
