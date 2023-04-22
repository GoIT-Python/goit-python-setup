import re

# text = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"
text = "Simple email cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com"

regex = r"[^ \t\n\r\f\v\d][a-zA-Z_.0-9]+@\w+\.\w{2,}"


def find_all_emails(text):
    result = re.findall(regex, text)
    return result


print(find_all_emails(text))

# Ожидалось, что функция find_all_emails при получении параметра:
# 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
# вернет следующий список:
# ['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']

# Ожидалось, что функция find_all_emails при получении параметра:
# 'Simple email cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com'
# вернет следующий список:
# ['cool@api.io', 'first.middle.last@iana.or', 'a2@test.com', 'a3@test.com']
