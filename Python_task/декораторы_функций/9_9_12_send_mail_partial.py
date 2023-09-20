from functools import partial


def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'


to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')
text = 'Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....'
send_an_invitation = partial(send_email, text=text)


print(send_an_invitation(name='Тимур', email_address='timyrik20@beegeek.ru'))
print(to_Timur('когда курс?'))