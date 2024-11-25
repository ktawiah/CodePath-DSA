class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def list_of_node(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next

    return result


def collect_false_evidence(evidence):
    visited = set()

    while evidence:
        if evidence.value not in visited:
            visited.add(evidence.value)
        else:
            next_node = evidence.next
            evidence.next = None
            return list_of_node(next_node)
        evidence = evidence.next

    return []


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

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))
