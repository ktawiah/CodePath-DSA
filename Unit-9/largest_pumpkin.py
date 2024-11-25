from is_balanced import build_tree
from collections import deque

"""Given the root of a binary tree pumpkin_patch where each node represents a pumpkin in the patch and each node value represents the pumpkin's size, return an array of the largest pumpkin in each row of the pumpkin patch. Each level in the tree represents a row of pumpkins.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity."""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def largest_pumpkins(pumpkin_patch):
    if not pumpkin_patch:
        return []

    queue = deque([(pumpkin_patch, 0)])
    level_nodes = []

    while queue:
        node, level = queue.popleft()

        if level + 1 > len(level_nodes):
            level_nodes.append([node.val])
        else:
            level_nodes[level].append(node.val)

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    for index, nodes in enumerate(level_nodes):
        level_nodes[index] = max(nodes)

    return level_nodes


"""
    1
   /  \
  3    2
 / \    \   
5   3    9
"""
# Using build_tree() function included at the top of the page
pumpkin_sizes = [1, 3, 2, 5, 3, None, 9]
pumpkin_patch = build_tree(pumpkin_sizes)

print(largest_pumpkins(pumpkin_patch))
