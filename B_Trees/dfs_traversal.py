class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_depth_first(root):
    result = []
    stack = [root]

    while stack:
        current_node = stack.pop()

        result.append(current_node.val)

        if current_node.right:
            stack.append(current_node.right)

        if current_node.left:
            stack.append(current_node.left)

    return result


tree = TreeNode(
    1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6))
)

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left, a.right = b, c
# b.left, b.right = d, e
# c.right = f

print(traverse_depth_first(tree))
