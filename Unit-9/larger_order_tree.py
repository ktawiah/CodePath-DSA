from is_balanced import print_tree, build_tree

"""You have the root of a binary search tree orders, where each node in the tree represents an order and each node's value represents the number of cupcakes the customer ordered. Convert the tree to a 'larger order tree' such that the value of each node in tree is equal to its original value plus the sum of all node values greater than it.

As a reminder a BST satisfies the following constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity."""

from collections import deque


def sum_tree(root):
    result_sum = 0

    if not root:
        return result_sum

    stack = [root]

    while stack:
        node = stack.pop()

        result_sum += node.val

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return result_sum


def larger_order_tree(orders):
    queue = deque([orders])

    while queue:
        node = queue.pop()

        node.val += sum_tree(node.right)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return orders


"""
         4
       /   \
      /     \
     1       6
    / \     / \
   0   2   5   7
        \       \
         3       8   
"""
if __name__ == "__main__":
    # using build_tree() function included at top of page
    order_sizes = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    orders = build_tree(order_sizes)

    # using print_tree() function included at top of page
    print_tree(larger_order_tree(orders))
