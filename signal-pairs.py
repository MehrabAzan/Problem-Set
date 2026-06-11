def find_difference(signals1, signals2):
    set1 = set(signals1)
    set2 = set(signals2)

    diff1 = set1 - set2
    diff2 = set2 - set1

    return [list(diff1), list(diff2)]

signals1_example1 = [1, 2, 3]
signals2_example1 = [2, 4, 6]

signals1_example2 = [1, 2, 3, 3]
signals2_example2 = [1, 1, 2, 2]

print(find_difference(signals1_example1, signals2_example1)) 
print(find_difference(signals1_example2, signals2_example2))