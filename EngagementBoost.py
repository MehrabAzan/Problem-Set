def engagement_boost(engagements):
    leftPointer = 0
    rightPointer = len(engagements) - 1
    while leftPointer < rightPointer:
        engagements[leftPointer] *= engagements[leftPointer]
        engagements[rightPointer] *= engagements[rightPointer]
        leftPointer += 1
        rightPointer -= 1
    engagements.sort()
    return engagements

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))