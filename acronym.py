def is_acronym(words, s):
    for i in range(len(words)):
        if words[i][0] != s[i]:
            print(False)
            return False
    print(True)
    return True

words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)