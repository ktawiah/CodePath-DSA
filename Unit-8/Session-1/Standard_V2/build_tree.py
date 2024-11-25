from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root: TreeNode):
    queue = deque([root])
    result_list = []

    while queue:
        current = queue.popleft()
        result_list.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result_list


tree = TreeNode(
    "Poseidon",
    TreeNode("Atlantis", TreeNode("Coral"), TreeNode("Pearl")),
    TreeNode("Oceania", TreeNode("Kelp", TreeNode("Reef"))),
)

print(print_tree(tree))
