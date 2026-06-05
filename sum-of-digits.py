def sum_of_digits(num):
    result = 0
    while num != 0:
        digit = num % 10
        result += digit
        num = num // 10
    return result

num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))