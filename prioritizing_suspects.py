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


def partition(suspect_ratings, threshold):
    # Create ll to store less and greater than nodes
    less_ll = Node(None)
    greater_ll = Node(None)

    greater_curr = greater_ll
    less_curr = less_ll

    current_node = suspect_ratings
    # Iterate through ll
    while current_node:

        if current_node.value > threshold:
            greater_curr.next = current_node
            greater_curr = greater_curr.next
        else:
            less_curr.next = current_node
            less_curr = less_curr.next

        current_node = current_node.next

    less_curr.next = None
    greater_curr.next = less_ll.next
    print_linked_list(greater_ll.next)


suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))
