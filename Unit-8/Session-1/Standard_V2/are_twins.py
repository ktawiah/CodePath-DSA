from collections import deque
from build_tree import TreeNode


def mertwins(root):
    if not root:
        return False
    # Create a queue for bfs
    queue = deque([root])

    # Perform bfs
    while queue:
        current = queue.popleft()

        if current.left:
            queue.append(current.left)

        # Check if value left node on left node added to queue is the same as that for the right
        if current.right:
            if queue and current.right.val == queue[-1].val:
                return True
            queue.append(current.right)

    # Return False
    return False


root1 = TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral"))
root2 = TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral"))
root3 = TreeNode("Merenby", None, TreeNode("Calypso"))

print(mertwins(root1))
print(mertwins(root2))
print(mertwins(root3))
