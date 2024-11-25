from is_balanced import print_tree, build_tree

"""A vampire has come to stay at the haunted hotel, but he can't see his reflection! What's more, he doesn't seem to be able to see the reflection of anything in the mirror! He's asked you to come to his aid and help him see the reflections of different thngs.

Given the root of a binary tree vampire, return the mirror image of the tree. The mirror image of a tree is obtained by flipping the tree along its vertical axis, meaning that the left and right children of all non-leaf nodes are swapped.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity."""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def mirror_tree(root):
    if not root:
        return root

    stack = [root]

    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return root


"""
      🧛‍♂️
     /   \
    💪🏼    🤳
    /      \
   👟       👞
"""
# Using build_tree() function included at the top of the page
body_parts = ["🧛‍♂️", "💪🏼", "🤳", "👟", None, None, "👞"]
vampire = build_tree(body_parts)


"""
      🎃
     /   \
    😈    🕸️
         /  \
       🧟‍♂️    👻
"""
spooky_objects = ["🎃", "😈", "🕸️", None, None, "🧟‍♂️", "👻"]
spooky_tree = build_tree(spooky_objects)

# Using print_tree() function included at the top of the page
print_tree(mirror_tree(vampire))
print_tree(mirror_tree(spooky_tree))
