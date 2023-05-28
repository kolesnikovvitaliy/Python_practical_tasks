def трудности_перевода(lst):
    m = set(lst[0])
    for i in range(1, len(lst)):
        m = set(m).intersection(lst[i])
        if len(m) == 0:
            return "Сериал снять не удастся"
    return ", ".join(sorted(m)) 

n = int(input())
lst = [input().lower().split(', ') for _ in range(n)]
print(трудности_перевода(lst))

# 6
# испанский, португальский, эсперанто, французский
# французский, испанский, эсперанто
# португальский, эсперанто, французский, испанский
# французский, английский, болгарский, испанский, эсперанто
# эсперанто, английский, русский, испанский, французский
# python, испанский, эсперанто, латышский, польский, французский

# 6
# испанский, португальский, эсперанто, французский
# французский, испанский, эсперанто
# португальский, эсперанто, французский, испанский
# французский, английский, болгарский, испанский, эсперанто
# эсперанто, английский, русский, испанский, французский
# python, испанский, эсперанто, латышский, польский, французский