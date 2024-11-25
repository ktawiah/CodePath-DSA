class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def get_longest_consecutive_integer(root):
    """
        1 -> (1, 1, 1)
      /   \
      (2, 1, 2)    4
      /\
      (3, 2, 3) 4
    """
    if not root:
        return 0

    max_count = float("-inf")
    stack = [(root, root.val - 1, 0)]

    while stack:
        curr_node, par_node_val, count = stack.pop()

        if not curr_node.left and not curr_node.right:
            max_count = max(count, max_count)
            count = 0

        if curr_node.val - par_node_val == 1:
            count += 1
        else:
            max_count = max(count + 1, max_count)
            count = 0

        if curr_node.right:
            stack.append((curr_node.right, curr_node.val, count))

        if curr_node.left:
            stack.append((curr_node.left, curr_node.val, count))

    return max_count + 1


# tree = TreeNode(
#     1,
#     TreeNode(2, TreeNode(3), TreeNode(4)),
#     TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))), TreeNode(4)),
# )

# new_tree = TreeNode(
#     1,
#     TreeNode(5, TreeNode(6, TreeNode(7), None), None),
#     TreeNode(2, TreeNode(4, TreeNode(5, None, TreeNode(6)))),
# )

new_tree = TreeNode(
    1,
    TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(4)),
    TreeNode(5, TreeNode(6), TreeNode(7)),
)
# tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5))), TreeNode(3))
print(get_longest_consecutive_integer(new_tree))
