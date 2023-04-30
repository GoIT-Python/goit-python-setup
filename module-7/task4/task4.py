s = " "


def is_integer(s):
    if len(s) == 0:
        return False
    elif not len(s) == 0:
        if s.strip().startswith("+") or s.strip().startswith("-"):
            return s.strip()[1:].isdigit()
        return s.strip().isdigit()
    else:
        return True


print(is_integer(s))
