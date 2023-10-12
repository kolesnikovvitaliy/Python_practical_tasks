def is_phone_number(phone):
    groups = phone.split('-')
    chars = ''.join(groups)
    return all(c.isdigit() for c in chars) and\
        len(chars) >= 11 and\
        chars.startswith(('7', '8'))


def get_all_numbers(text):
    for c in range(len(text)):
        chunk = text[c:c + 15]
        if is_phone_number(chunk):
            lst = chunk.split('-')
            if all((lst[0] == '7', len(lst[1]) == 3, len(lst[2]) == 3)):
                yield chunk
            elif all((lst[0] == '8', len(lst[1]) == 3, len(lst[2]) == 2 or len(lst[2]) == 4)):
                yield chunk


txt = input()
[print(i) for i in get_all_numbers(txt)]
# Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911

# 7-919-667-21-19
# 8-917-4864-1911