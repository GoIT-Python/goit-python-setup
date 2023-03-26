def format_string(string, length=1):
    if len(string) >= length:
        return string
    else:
        return " " * ((length - len(string)) // 2) + string


print(format_string(length=15, string="abaa"))

# string='aaaaaaaaaaaaaaaaac', length=12

# length=15, string='abaa'
