def exclusive_elemts(lst1, lst2):
    lst = []
    for word1 in lst1:
        counter = 0

        for word2 in lst2:
            if word1 == word2:
                counter += 1

        if counter == 0:
            lst.append(word1)
    
    for word2 in lst2:
        counter = 0

        for word1 in lst1:
            if word1 == word2:
                counter += 1

        if counter == 0:
            lst.append(word2)

    print(lst)
    return lst

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)