def is_valid_post_format(posts):
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    for char in posts:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False
    return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))
