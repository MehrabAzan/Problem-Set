def are_equivalent(word1, word2):
    total1 = ""
    total2 = ""

    for word in word1:
        total1 += word
    for word in word2:
        total2 += word

    if total1 == total2:
        print(True)
    else:
        print(False)

word1 = ["bat", "man"]
word2 = ["b", "atman"]
are_equivalent(word1, word2)

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
are_equivalent(word1, word2)

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
are_equivalent(word1, word2)