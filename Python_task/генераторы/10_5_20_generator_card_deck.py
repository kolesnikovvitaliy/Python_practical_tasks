def card_deck(suit):
    card = [f'{j} {i}' for i in ('пик', 'треф', 'бубен', 'червей')
            if i != suit for j in (*[i for i in range(2, 11)],
                                   'валет', 'дама', 'король', 'туз')]
    # count = 0
    # while True:
    #     if count == len(card):
    #         count = 0
    #     yield card[count]
    #     count += 1
    while True:
        yield from card
