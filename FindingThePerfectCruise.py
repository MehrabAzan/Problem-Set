def find_cruise_length(cruise_lengths, vacation_length):
    left, right = 0, len(cruise_lengths) - 1
    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1
            mid = left // 2
        else:
            right = mid - 1
            mid = right // 2
    return False

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))