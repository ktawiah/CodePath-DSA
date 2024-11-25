"""Leaning into the haunted hotel aesthetic, you've begun growing a pumpkin patch behind the hotel for the upcoming Halloween season. Given the root of a binary tree where each node represents a section of a pumpkin patch with a certain number of pumpkins, find the root-to-leaf path that yields the largest number of pumpkins. Return a list of the node values along the maximum pumpkin path.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity."""

from is_balanced import build_tree


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def max_pumpkins_path(root):
    stack = [(root, [])]

    result = []

    while stack:
        node, n_list = stack.pop()

        new_path = n_list + [node.val]

        if not node.left and not node.right:
            result.append(new_path)

        if node.right:
            stack.append((node.right, new_path))

        if node.left:
            stack.append((node.left, new_path))

    sum_nodes, index = float("-inf"), 0

    for idx, nodes in enumerate(result):
        if sum(nodes) > sum_nodes:
            sum_nodes = sum(nodes)
            index = idx

    return result[index]


"""
    7
   / \
  3   10
 /   /  \
1   5    15
"""
# Using build_tree() function includedd at the top of the page
pumpkin_quantities = [7, 3, 10, 1, None, 5, 15]
root1 = build_tree(pumpkin_quantities)

"""
    12
   /  \
  3     8
 / \  /   \
4   50    10
"""
pumpkin_quantities = [12, 3, 8, 4, 50, None, 10]
root2 = build_tree(pumpkin_quantities)

print(max_pumpkins_path(root1))
print(max_pumpkins_path(root2))
