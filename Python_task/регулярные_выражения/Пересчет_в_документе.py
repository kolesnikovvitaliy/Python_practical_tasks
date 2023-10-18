import re
text = 'GROHE Aria 25081000 - Смеситель для ванны (хром) - $558  $1 SCBRHMI Серийный ЖК-дисплей HMI TFT с сенсорной панелью 10,4 дюйма - $95,25 Кран шаровый 1" наружная резьба - нет в продаже GROHE Aria 25081000 - Смеситель для ванны (хром) - $558'
D = 59.5
S = 2.54


def convert_item(item):
    tmp = str(item)
    if '.' in tmp:
        x = tmp.split('.')
        if len(x[1]) == 1 and x[1] == '0':
            return int(x[0])
        return re.sub(r"\.", r",", tmp)
    elif ',' in tmp:
        return float(re.sub(r",", r".", tmp))
    return float(tmp)


def func(m):
    if '$' in m[0]:
        items, flag, sim = convert_item(m[0][1:]), 'руб', D
    else:
        items, flag, sim = convert_item(re.search(r'[0-9,]+', m[0]).group()), 'см', S
    return f'{convert_item(round(items*sim, 2))} {flag}'


print(re.sub(r'((\$[0-9,]+\b)|([0-9,]+\sдюйма\b)|([0-9,]+\"))', func, text))
