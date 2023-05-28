def spell(*lst):
    words = {}
    for i in lst: 
        if i[0].lower() not in words:
            words[i[0].lower()] = len(i.lower())
        else:
            if len(i.lower()) > words[i[0].lower()]:
                words[i[0].lower()] = len(i.lower())
    return words
    # s = {i[0].lower():len(i) for i in sorted(words,key=len)}
    # return s
    
words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))
#{'р': 7, 'а': 9, 'у': 10, 'к': 5}