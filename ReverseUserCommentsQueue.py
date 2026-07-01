def reverse_comments_queue(comments):
    stack = []
    for comment in comments:
        stack.append(comment)
    reversedComments = []
    while len(stack) > 0:
        reversedComments.append(stack.pop())
    return reversedComments

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))