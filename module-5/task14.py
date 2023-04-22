import re

text = "Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787"
regex = r"[+]\d{3}[(]\d{2}[)]\d{3}[-][\d][\d|-]{2}\d{2}"


def find_all_phones(text):
    result = re.findall(regex, text)
    return result


print(find_all_phones(text))

# Ожидалось, что функция find_all_phones при получении параметра:
# 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'
# вернет следующий список:
# ['+380(67)777-7-771', '+380(67)777-77-77', '+380(67)777-77-78']
