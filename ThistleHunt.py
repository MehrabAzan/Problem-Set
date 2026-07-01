def locate_thistles(items):
    nums = []
    for i in range(len(items)):
        if items[i] == "thistle":
            nums.append(i)
    return nums

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))