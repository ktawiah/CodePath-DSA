from collections import deque


def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root


# Problem 3: Maximum Tiers in Cake
# You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake, where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different section of your cake, return the maximum number of tiers in your cake.

# The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def max_tiers(cake):
    if not cake:
        return 0

    stack = [(cake, 0)]
    max_count = float("-inf")

    while stack:
        node, count = stack.pop()

        if not node.left and not node.right:
            max_count = max(max_count, count)

        if node.right:
            stack.append((node.right, count + 1))

        if node.left:
            stack.append((node.left, count + 1))

    return max_count + 1


"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = [
    "Chocolate",
    "Vanilla",
    "Strawberry",
    None,
    None,
    "Chocolate",
    "Coffee",
]
cake = build_tree(cake_sections)
# print(cake)

print(max_tiers(cake))
# def merge_orders(order1, order2):
#     stack1, stack2 = [order1], [order2]

#     while stack1 and stack2:
#         node1, node2 = stack1.pop(), stack2.pop()

#         node1.val = (node1.val if node1 else 0) + (node2.val if node2 else 0)

#         if node1.left:
#             stack1.append(node1.left)

#         if node1.right:
#             stack1.append(node1.right)

#         if node2.left:
#             stack2.append(node2.left)

#         if node2.right:
#             stack2.append(node2.right)

#     return order1


# """
#      1             2
#     /  \         /   \
#    3    2       1     3
#  /               \      \
# 5                 4      7
# """
# # Using build_tree() function included at top of page
# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)

# # Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))
