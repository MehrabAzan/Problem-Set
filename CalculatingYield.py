class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    x = root.left.val
    y = root.right.val
    total = 0
    if root.val == "+":
        total = (x + y)
    if root.val == "-":
        total = (x - y)
    if root.val == "*":
        total = (x * y)
    if root.val == "/":
        total = (x / y)
    return total

"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))