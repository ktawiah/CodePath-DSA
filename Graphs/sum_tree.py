from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_tree_recursive(root: TreeNode):
    if not root:
        return 0

    return root.val + sum_tree_recursive(root.left) + sum_tree_recursive(root.right)


def sum_of_tree(root: TreeNode):
    if not root:
        return None

    queue = deque([root])
    total = 0

    while queue:
        node = queue.popleft()

        total += node.val

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return total


if __name__ == "__main__":
    tree = TreeNode(
        4,
        TreeNode(3, TreeNode(9), TreeNode(7)),
        TreeNode(6, TreeNode(10, TreeNode(12))),
    )
    # print(sum_of_tree(tree))
    print(sum_tree_recursive(tree))
