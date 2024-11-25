class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, target):
    result = []

    stack = [(root, [], 0)]

    while stack:
        node, par_path, par_sum = stack.pop()

        par_path.append(node.val)
        par_sum += node.val

        if not node.left and not node.right and par_sum == target:
            result.append(par_path)

        if node.left:
            stack.append((node.left, par_path.copy(), par_sum))

        if node.right:
            stack.append((node.right, par_path.copy(), par_sum))

    return result


if __name__ == "__main__":
    tree = TreeNode(
        4, TreeNode(7, TreeNode(1), TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(1))
    )
    print(path_sum(tree, 7))
