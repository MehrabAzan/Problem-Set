def move_zeroes(lst):
    count = 0

    for num in lst:
        if num == 0:
            count += 1
    
    for i in range(count):
        lst.remove(0)
        lst.append(0)

    result = lst
    return result

lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst))