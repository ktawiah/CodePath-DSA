from collections import deque
from unittest.mock import right


# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# def calculate_yield(root):
#     if not root:
#         return 0
#
#     if root.val in {"+", "-", "*", "/"}:
#         return root.left.val + root.right.val
#
# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
#
# print(calculate_yield(apple_tree))
from collections import deque
def right_vine(root):
    queue = deque()
    queue.append(root)
    result = [root.val]

    while queue:
        current = queue.popleft()

        if current.left:
            queue.append(current.left)

        if current.right:
            result.append(current.right.val)
            queue.append(current.right)

    return result
    # if result is None:
    #     result = []
    #
    # if root is None:
    #     return result
    #
    # result.append(root.val)
    #
    # return right_vine(root.right, result)
ivy1 = TreeNode("Root",
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))