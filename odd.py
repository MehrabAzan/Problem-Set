def get_odds(nums):
    array = []
    for num in nums:
        if num % 2 == 1:
            array.append(num)
    return array

nums = [1, 2, 3, 4]
print(get_odds(nums))

nums = [2, 4, 6, 8]
print(get_odds(nums))