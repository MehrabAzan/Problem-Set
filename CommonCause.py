def common_elements(lst1, lst2):
    lst = []
    for s1 in lst1:
        for s2 in lst2:
            if s1 == s2:
                lst.append(s1)
    return lst

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
print(common_elements(lst1, lst2))

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
print(common_elements(lst1, lst2))