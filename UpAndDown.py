def up_and_down(lst):
    odd = 0
    even = 0
    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd - even

lst = [1, 2, 3]
print(up_and_down(lst))

lst = [1, 3, 5]
print(up_and_down(lst))

lst = [2, 4, 10, 2]
print(up_and_down(lst))