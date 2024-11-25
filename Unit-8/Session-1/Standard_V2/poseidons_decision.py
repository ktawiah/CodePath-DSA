from build_tree import TreeNode


def get_decision(root):
    if not root:
        return -1

    if not root.left and not root.right:
        return root.val

    if root.val == "OR":
        return root.left.val or root.right.val
    else:
        return root.left.val and root.right.val


"""
        OR
      /    \
    True  False
"""
expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))

"""
       False
"""
expression2 = TreeNode(False)

print(get_decision(expression1))
print(get_decision(expression2))
print(get_decision(TreeNode("AND", TreeNode(True), TreeNode(True))))
