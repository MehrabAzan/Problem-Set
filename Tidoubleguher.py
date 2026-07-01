def tiggerfy(s):
    newS = ""
    for c in s:
        if c not in "tigerTIGER":
            newS += c
    return newS

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))