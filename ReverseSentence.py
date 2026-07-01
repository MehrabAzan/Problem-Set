def reverse_sentence(sentence):
    stack = []

    for word in sentence.split():
        stack.append(word)
    
    reverseSentence = []

    while stack:
        reverseSentence.append(stack.pop())

    result = " ".join(reverseSentence)
    return result

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))