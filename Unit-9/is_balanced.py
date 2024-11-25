from collections import deque


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


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# def is_balanced(display):
#     if not display:
#         return True

#     stack = [display]

#     while stack:
#         curr = stack.pop()

#         if (curr.left and not curr.right) or (curr.right and not curr.left):
#             return False

#         if curr.right:
#             stack.append(curr.right)

#         if curr.left:
#             stack.append(curr.left)

#     return True


# def is_balanced(display):
#     if not display:
#         return True

#     if (display.left and not display.right) or (not display.left and display.right):
#         return False

#     left_vals = is_balanced(display.left)
#     right_vals = is_balanced(display.right)
#     return left_vals and right_vals


# """
#       🎂
#      /  \
#    🥮   🍩
#        /  \
#      🥖    🧁

# """
# # Using build_tree() function included at top of page
# baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
# display1 = build_tree(baked_goods)

# """
#           🥖
#          /  \
#        🧁    🧁
#        /       \
#       🍪       🍪
#      /           \
#     🥐           🥐

# """
# baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
# display2 = build_tree(baked_goods)


# print(is_balanced(display1))
# print(is_balanced(display2))

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


def sum_each_days_orders(orders):
    if not orders:
        return []

    queue = deque([(orders, 0)])
    result = []

    while queue:
        curr_node, height = queue.popleft()

        if height + 1 > len(result):
            result.append(curr_node.val)
        else:
            result[height] += curr_node.val

        if curr_node.left:
            queue.append((curr_node.left, height + 1))

        if curr_node.right:
            queue.append((curr_node.right, height + 1))

    return result


"""
      4
     / \
    2   6
   / \  
  1   3
"""
if __name__ == "__main__":
    # Using build_tree() function included at top of page
    order_sizes = [4, 2, 6, 1, 3]
    orders = build_tree(order_sizes)

    print(sum_each_days_orders(orders))
