def cхожие_буквы(lst):
    a = set()
    for i in lst:
        if i in ru:
            a.add('ru')
        elif i in en:
            a.add('en') 
    return 'mix' if len(a) > 1 else [*a][0]
en = "AaBCcEeHKMOoPpTXxy"
ru = "АаВСсЕеНКМОоРрТХху"

lst = [input() for _ in range(3)]
print(cхожие_буквы(lst))