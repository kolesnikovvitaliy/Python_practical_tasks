def hide_card(card):
    #card = card.replace(" ", "")
    #return f'************{card[-4:]}'
    return '*' * 12 + card.replace(' ', '')[-4:]
    #return '*'*12+''.join(card_number.split())[12:]

card = '  1 2 3 4 5 6 7 8      9 0 1 2 3 4 5 6  '

print(hide_card(card))