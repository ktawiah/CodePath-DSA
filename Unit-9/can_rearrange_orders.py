from is_balanced import TreeNode, build_tree

"""In your bakery, customer orders are each represented by a binary tree. The value of each node in the tree represents a type of cupcake, and the tree structure represents how the order is organized in the delivery box. Sometimes, orders don't get picked up.

Given two orders, you want to see if you can rearrange the first order that didn't get picked up into the second order so as not to waste any cupcakes. You can swap the left and right subtrees of any cupcake (node) in the order.

Given the roots of two binary trees order1 and order2, write a function can_rearrange_orders() that returns True if the tree represented by order1 can be rearranged to match the tree represented by order2 by doing any number of swaps of order1’s left and right branches.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""


def can_rearrange_orders(order1, order2):
    stack1, stack2 = [order1], [order2]

    # Iterate df on both trees
    while stack1 and stack2:
        node1, node2 = stack1.pop(), stack2.pop()

        # Update nodes inversely
        if node1.left:
            stack1.append(node1.left)

        if node2.right:
            stack2.append(node2.right)

        if node1.right:
            stack1.append(node1.right)

        if node2.left:
            stack2.append(node2.left)

    # Check if either stack is not empty
    if stack1 or stack2:
        return False

    return True


"""
              Red Velvet                             Red Velvet
             /          \                           /           \
        Vanilla         Lemon                   Lemon            Vanilla
        /      \        /   \                  /     \           /      \
      Ube    Almond  Chai   Carrot       Carrot      Chai    Almond    Ube 
                     /   \        \       /          /   \      
                 Chai   Maple   Smore   Smore    Maple   Chai
"""

# Using build_tree() function included at top of page
flavors1 = [
    "Red Velvet",
    "Vanilla",
    "Lemon",
    "Ube",
    "Almond",
    "Chai",
    "Carrot",
    None,
    None,
    None,
    None,
    "Chai",
    "Maple",
    None,
    "Smore",
]
flavors2 = [
    "Red Velvet",
    "Lemon",
    "Vanilla",
    "Carrot",
    "Chai",
    "Almond",
    "Ube",
    "Smore",
    None,
    "Maple",
    "Chai",
]
if __name__ == "__main__":
    order1 = build_tree(flavors1)
    order2 = build_tree(flavors2)

    print(can_rearrange_orders(order1, order2))
