def concatenate(words):
    total = ""
    for word in words:
        total += word
    return total

words = ["vengeance", "darkness", "batman"]
print(concatenate(words))

words = []
print(concatenate(words))