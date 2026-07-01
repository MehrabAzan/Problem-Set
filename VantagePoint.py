def highest_altitude(gain):
    currAltitude = 0
    lst = []
    for i in range(len(gain)):
        currAltitude += gain[i]
        lst.append(currAltitude)
    if max(lst) < 0:
        return 0
    return max(lst)

gain = [-5, 1, 5, 0, -7]
print(highest_altitude(gain))

gain = [-4, -3, -2, -1, 4, 3, 2]
print(highest_altitude(gain))