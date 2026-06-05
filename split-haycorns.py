def split_haycorns(quantity):
    array = []
    for num in range(quantity):
        if quantity % (num + 1) == 0:
            array.append(num + 1)
    return array

quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))