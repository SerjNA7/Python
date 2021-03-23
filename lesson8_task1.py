import re

def email_parse(email_adress):
    email = re.compile(r'(?P<user_name>([\w]+))@(?P<domine>[^&]+\.\w+)', re.IGNORECASE)
    if not email.match(email_adress):
        raise ValueError(f'wrong email: {email_adress}')
    print(email.match(email_adress).groupdict())

try:
    email_parse('nesterovsa@geekbrains.ru')
    email_parse('nesyErovsa@geekbrains.ru')
    email_parse('ne0ter-vsa@geekbrains.ru')
    email_parse('ne/teroesa.@geekbrains.ru')
except ValueError as error:
    print(error)