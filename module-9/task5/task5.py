import functools

# phone = "    +38(050)123-32-34"
# phone = "     0503451234"
# phone = "(050)8889900"
# phone = "38050-111-22-22"
phone = "38050 111 22 11   "


def format_phone_number(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if len(res) < 12:
            prefix = "+38"
        else:
            prefix = "+"
        res = prefix + res
        return res

    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


print(sanitize_phone_number(phone))
