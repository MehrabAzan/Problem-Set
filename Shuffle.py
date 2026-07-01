def shuffle(cards):
    lst = []
    for i in range(len(cards) // 2):
        lst.append(cards[i])
        lst.append(cards[i + len(cards) // 2])
    return lst

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))