class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def post_order(root):
    result = []

    if not root:
        return result

    stack = [(root, False)]

    while stack:
        node, visited = stack.pop()

        if node:
            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))

    return result


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)
tree = TreeNode(1, None, TreeNode(2, TreeNode(3), None))

print(post_order(tree))
