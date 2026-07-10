class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    curr = clues
    head = clues
    while curr:
        if curr.next == head:
            return True
        else:
            curr = curr.next
    return False

# time complexity: O(n)
# space complexity: O(1)

def collect_false_evidence(evidence):
    values = []
    slow = fast = evidence
    while fast and fast.next:
        if slow == fast:
            return slow
        else:
            slow = slow.next
            fast = fast.next.next
    return 

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print("\n")
print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))