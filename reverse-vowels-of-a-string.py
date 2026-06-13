def reverse_vowels(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] not in "aeiouAEIOU":
            left += 1
        elif s[right] not in "aeiouAEIOU":
            right -= 1
        else:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
    result = "".join(s)
    return result

s = "robin"
print(reverse_vowels(s))

s = "BATgirl"
print(reverse_vowels(s))

s = "batman"
print(reverse_vowels(s))