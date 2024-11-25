from is_balanced import build_tree, deque, print_tree, TreeNode

"""There are unwanted visitors lurking in the rooms of your haunted hotel, and it's time for a clear out. Given the root of a binary tree hotel where each node represents a room in the hotel and each node value represents the guest staying in that room. You want to systematically remove visitors in the following order:

Collect the guests (values) of all leaf nodes and store them in a list. The leaf nodes may be stored in any order.
Remove all the leaf nodes.
Repeat until the hotel (tree) is empty.
Return a list of lists, where each inner list represents a collection of leaf nodes.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity."""


# from collections import deque


def purge_hotel(hotel):
    leaf_nodes = []

    # Edge case: if the tree is empty
    if not hotel:
        return leaf_nodes

    while hotel:
        queue = deque([hotel])
        new_leaves = []

        # Level-order traversal to find leaf nodes
        while queue:
            node = queue.popleft()

            # If it's a leaf node, collect its value
            if not node.left and not node.right:
                new_leaves.append(node.val)

            # Otherwise, add the child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # After collecting all leaves, append to the result
        leaf_nodes.append(new_leaves)

        # Now, remove the leaf nodes from the tree by updating parents
        def remove_leaves(node):
            if not node:
                return None
            if not node.left and not node.right:
                return None  # This is a leaf, so remove it
            node.left = remove_leaves(node.left)
            node.right = remove_leaves(node.right)
            return node

        # Re-assign the root of the tree after removing the leaves
        hotel = remove_leaves(hotel)

    return leaf_nodes


"""
      👻
     /  \
   😱   🧛🏾‍♀️
  /  \
 💀  😈
"""

# Using build_tree() function included at the top of the page
guests = ["👻", "😱", "🧛🏾‍♀️", "💀", "😈"]
hotel = build_tree(guests)

# Using print_tree() function included at the top of the page
print_tree(hotel)
print(purge_hotel(hotel))
