def count_suits_iterative(suits):
    uniqueSuits = set(suits)
    return len(uniqueSuits)

def count_suits_recursive(suits):
    if not suits:
        return 0


print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))