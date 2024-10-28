class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def traverse_depth_first(root):
    result = []
    stack = [root]
    visited = set()

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            result.append(current_node.val)

            if current_node.right:
                stack.append(current_node.right)

            if current_node.left:
                stack.append(current_node.left)

    return result


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left, a.right = b, c
b.left, b.right = d, e
c.right = f

print(traverse_depth_first(a))
