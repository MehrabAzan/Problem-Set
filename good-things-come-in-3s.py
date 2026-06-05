def make_divisible_by_3(nums):
    result = 0
    for num in nums:
        if num % 3 != 0:
            num += 1
            if num % 3 != 0:
                num -= 2
                result += 1
            else:
                result += 1
    print(result)
    return result

nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)