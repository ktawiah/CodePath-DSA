class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    # heights = []
    stack = [(root, 0)]
    max_height = float("-inf")

    while stack:
        node, height = stack.pop()

        if not node.left and not node.right:
            max_height = max(max_height, height + 1)

        if node.right:
            stack.append((node.right, height + 1))

        if node.left:
            stack.append((node.left, height + 1))

    return max_height


a = Node(3, Node(11, Node(4), Node(-2)), Node(4, Node(1)))

print(max_path_sum(a))
