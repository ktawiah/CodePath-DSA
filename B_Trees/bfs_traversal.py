from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_breath_first(root):
    result = []
    if root is None:
        return result

    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        result.append(current_node.val)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return result


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left, a.right = b, c
# b.left, b.right = d, e
# c.right = f

# root = Node(1)
# root.left = Node(2)
# root.right = Node(1)
# root.left.left = Node(2)
# root.left.right = Node(3)

tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))


print(traverse_breath_first(tree))
