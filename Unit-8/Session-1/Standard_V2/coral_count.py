"""Due to climate change, you have noticed that coral has been dying in the reef near Atlantis. You want to ensure there is still a healthy level of coral in the reef. Given the root of a binary tree where each node represents a coral in the reef, write a function count_coral() that returns the number of corals in the reef.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def count_coral(root):
    if not root:
        return 0

    stack = [root]
    count = 0

    while stack:
        current = stack.pop()
        count += 1

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return count


"""
          Staghorn
         /        \
        /          \
    Sea Fan      Sea Whip
    /     \       /   
 Bubble  Table  Star
  /
Fire
"""
reef1 = TreeNode(
    "Staghorn",
    TreeNode("Sea Fan", TreeNode("Bubble", TreeNode("Fire")), TreeNode("Table")),
    TreeNode("Sea Whip", TreeNode("Star")),
)

"""
     Fire
    /    \
   /      \ 
Black    Star
        /  
     Lettuce 
           \
        Sea Whip
"""
reef2 = TreeNode(
    "Fire",
    TreeNode("Black"),
    TreeNode("Star", TreeNode("Lettuce", None, TreeNode("Sea Whip"))),
)

print(count_coral(reef1))
print(count_coral(reef2))
