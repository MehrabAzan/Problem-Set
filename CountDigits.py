def count_digits(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

n = 964
print(count_digits(n))

n = 0
print(count_digits(n))