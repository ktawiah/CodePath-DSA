class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def leftmost_path(root):
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        current = stack.pop()
        result.append(current.val)

        if current.left:
            stack.append(current.left)

    return result


def leftmost_path_recursive(root, result=None):
    if not result:
        result = []
    if not root:
        return []
    return [root.val] + leftmost_path_recursive(root.left)


"""
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF  
"""
system_a = TreeNode(
    "CaveA",
    TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")),
    TreeNode("CaveC", None, TreeNode("CaveF")),
)

"""
  CaveA
      \
      CaveB
        \
        CaveC  
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path_recursive(system_a))
print(leftmost_path_recursive(system_b))
