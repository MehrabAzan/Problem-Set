def left_right_difference(nums):
    answer = []
    left_sum = 0
    right_sum = 0
    if len(nums) == 1:
        answer = [0]
        return answer
    for i in range(len(nums)):
        if i == 0:
            left_sum = 0
            right_sum = sum(nums[1:len(nums)])
        elif i == len(nums) - 1:
            right_sum = 0
            left_sum = sum(nums[0:len(nums) - 1])
        else:
            left_sum = sum(nums[0:i])
            right_sum = sum(nums[i + 1:len(nums)])
        answer.append(left_sum - right_sum)
    return answer

nums = [10, 4, 8, 3]
print(left_right_difference(nums))

nums = [1]
print(left_right_difference(nums))