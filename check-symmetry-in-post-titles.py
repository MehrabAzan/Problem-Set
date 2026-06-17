def is_symmetrical_title(title):
    leftPointer = 0
    rightPointer = len(title) - 1
    while leftPointer < rightPointer:
        if not title[leftPointer].isalnum():
            leftPointer += 1
        if not title[rightPointer].isalnum():
            rightPointer -= 1
        if title[leftPointer].lower() != title[rightPointer].lower():
            return False
        leftPointer += 1
        rightPointer -= 1
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 