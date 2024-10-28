class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    # Create a list of nodes
    node_list = []
    for val in values:
        node_list.append(Node(val))

    # Update next pointers of each node
    index = 0
    while index < len(node_list) - 2:
        node_list[index].next = node_list[index + 1]
        index += 1

    # Return head node
    return node_list[0]


def printll(head):
    current = head

    while current:
        print(current.val, end="->")
        current = current.next


print(printll(create_linked_list([2, 3, 4])))
