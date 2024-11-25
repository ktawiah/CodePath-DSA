from is_balanced import TreeNode


def bst_from_preorder(preorder):
    if not preorder:
        return None

    root = TreeNode(preorder.pop(0))
    stack = [root]

    while preorder:
        val = preorder.pop(0)
        node = TreeNode(val)

        # Check if the node should be the left child of the last item in the stack
        if val < stack[-1].val:
            stack[-1].left = node
        else:
            # Find the correct parent node by popping elements from the stack
            while stack and stack[-1].val < val:
                parent = stack.pop()
            parent.right = node

        # Push the new node onto the stack
        stack.append(node)

    return root
