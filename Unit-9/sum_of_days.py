from is_balanced import build_tree, TreeNode

"""Your bakery stores each customer order in a binary tree, where each node represents a different customer's order and each node value represents the number of cookies ordered. Each level of the tree represents the orders for a given day.

Given the root of a binary tree orders, return a list of the sums of all cookies ordered in each day (level) of the tree.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity."""

from collections import deque


def sum_each_days_orders(orders):
    if not orders:
        return []

    # Create a result list
    result = []

    # Perform a bfs and keep track of each node and height in the tree
    queue = deque([(orders, 0)])

    # Check if len of result list corresponds to current height of tree
    while queue:
        node, height = queue.popleft()

        # Update result list
        if height + 1 > len(result):
            result.append([node.val])
        else:
            result[height].append(node.val)

        if node.left:
            queue.append((node.left, height + 1))

        if node.right:
            queue.append((node.right, height + 1))

    # Iterate through result list and update list in-place with diff.
    for index, node_val in enumerate(result):
        result[index] = abs(max(node_val) - min(node_val))

    # Return result list
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
