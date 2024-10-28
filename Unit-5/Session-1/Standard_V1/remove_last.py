"""
Write a function delete_tail() that accepts the head of a linked list and removes the last node in the list. Return the head of the modified list.

Note: The "tail" of a list is the last element in the linked list. It is equivalent to lst[-1] in a normal list.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def delete_tail(head):
    # Keep tack of the current node
    current_node = head

    # Traverse through the linked list
    while current_node:

        # Keep track of the next node
        next_node = current_node.next

        # Check if at the tail
        if next_node.next is None:
            # Assign next node of previous node to a null node
            current_node.next = None
            next_node = None
            break

        current_node = current_node.next

    return head

    # Set current node to null


butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))
