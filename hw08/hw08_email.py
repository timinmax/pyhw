import re

re_mail = re.compile(r'(^[a-zA-Z0-9\.\-_]+)[@]{1}([a-zA-Z0-9\.\-_]+\.[a-zA-Z]{2,3}$)')


def email_parse(str_to_parse):
    user_domain = re_mail.findall(str_to_parse)
    if len(user_domain) < 1:
        raise ValueError(f'{str_to_parse} is invalid email')
    return {'username': user_domain[0][0], 'domain':  user_domain[0][1]}


print(email_parse("asd.dd@ffa.ru"))#{'username': 'asd.dd', 'domain': 'ffa.ru'}
print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
print(email_parse("+++##@ffa.ru"))
