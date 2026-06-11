def nanana_batman(x):
    if x == 0:
        print("batman!")
    else:
        s = ""
        for i in range(x):
            s += "na"
        print(f"{s} batman!")

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)