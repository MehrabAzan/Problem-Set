def merge_alternately(word1, word2):
    result = ""

    while word1 or word2:
        if word1 and word2:
            result += word1[0] + word2[0]
            word1 = word1[:0] + word1[1:]
            word2 = word2[:0] + word2[1:]
        elif word1:
            result += word1[0]
            word1 = word1[:0] + word1[1:]
        elif word2:
            result += word2[0]
            word2 = word2[:0] + word2[1:]

    print(result)
    return result

word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)