# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode):
    if not root:
        return []

    stack, current = [], root
    result = []

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)

        current = current.right

    return result


# def inorder_traversal(root):
#     result = []
#     stack = []
#     current_node = root

#     while stack or current_node:
#         while current_node:
#             stack.append(current_node)
#             current_node = current_node.left

#         current_node = stack.pop()
#         result.append(current_node.val)

#         current_node = current_node.right

#     return result


# Example 1: Simple tree with 3 nodes
#      1
#     / \
#    2   3
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# Example 2: Unbalanced tree (left-heavy)
#       1
#      /
#     2
#    /
#   3
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.left.left = TreeNode(3)

# Example 3: Full binary tree
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7
tree3 = TreeNode(1)
tree3.left = TreeNode(2)
tree3.right = TreeNode(3)
tree3.left.left = TreeNode(4)
tree3.left.right = TreeNode(5)
tree3.right.left = TreeNode(6)
tree3.right.right = TreeNode(7)

# Example 4: Tree with a single node
#    1
tree4 = TreeNode(1)

# Example 5: Unbalanced tree (right-heavy)
#    1
#     \
#      2
#       \
#        3
tree5 = TreeNode(1)
tree5.right = TreeNode(2)
tree5.right.right = TreeNode(3)


# Instantiate the Solution class

# Test on Example 1
print("Inorder Traversal of Tree 1:", inorder_traversal(tree1))  # Output: [2, 1, 3]

# Test on Example 2
print("Inorder Traversal of Tree 2:", inorder_traversal(tree2))  # Output: [3, 2, 1]

# Test on Example 3
print(
    "Inorder Traversal of Tree 3:", inorder_traversal(tree3)
)  # Output: [4, 2, 5, 1, 6, 3, 7]

# Test on Example 4
print("Inorder Traversal of Tree 4:", inorder_traversal(tree4))  # Output: [1]

# Test on Example 5
print("Inorder Traversal of Tree 5:", inorder_traversal(tree5))  # Output: [1, 2, 3]
