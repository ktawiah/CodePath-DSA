class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    stack = [(root, 0)]
    max_sum = float("-inf")

    while stack:
        node, total = stack.pop()

        if not node.left and not node.right:
            max_sum = max(total + node.val, max_sum)

        if node.left:
            stack.append((node.left, total + node.val))

        if node.right:
            stack.append((node.right, total + node.val))

    return max_sum


# def max_path_sum(root):
#     if not root:
#         return 0

#     max_sum = float("-inf")  # This will store the overall maximum path sum
#     stack = [(root, 0)]  # Stack stores tuples of (node, current path sum)
#     result_sum = []

#     # Use a map to store the maximum path sum from each node
#     # node_sum = {}

#     while stack:
#         node, parent_sum = stack.pop()

#         # Compute the current node's sum (itself + the sum from parent)
#         current_sum = node.val + parent_sum

#         # Update the global max_sum (we take the max sum for this node + children)
#         max_sum = max(max_sum, current_sum)
#         if not node.right and not node.left:
#             result_sum.append(current_sum)

#         # Now process the children
#         if node.left:
#             stack.append((node.left, current_sum))
#         if node.right:
#             stack.append((node.right, current_sum))

#     # After traversal, return the maximum path sum found
#     print(result_sum)
#     return max_sum


a = Node(3, Node(11, Node(4), Node(-2)), Node(4, Node(1)))

print(max_path_sum(a))
