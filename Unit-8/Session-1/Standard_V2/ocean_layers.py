class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def ocean_depth(root):
    stack = [(root, 0)]
    result = []

    while stack:
        curr_node, parent_height = stack.pop()

        if not curr_node.left and not curr_node.right:
            result.append(parent_height + 1)

        if curr_node.right:
            stack.append((curr_node.right, parent_height + 1))

        if curr_node.left:
            stack.append((curr_node.left, parent_height + 1))

    return max(result)


"""
                Sunlight
               /        \
              /          \
          Twilight      Squid
         /       \           \   
      Abyss  Anglerfish    Giant Squid
      /
  Trenches
"""
ocean = TreeNode(
    "Sunlight",
    TreeNode(
        "Twilight", TreeNode("Abyss", TreeNode("Trenches")), TreeNode("Anglerfish")
    ),
    TreeNode("Squid", TreeNode("Giant Squid")),
)

"""
    Spray Zone
    /         \
   /           \ 
Beach       High Tide
            /  
      Middle Tide
              \
            Low Tide
"""
tidal_zones = TreeNode(
    "Spray Zone",
    TreeNode("Beach"),
    TreeNode("High Tide", TreeNode("Middle Tide", None, TreeNode("Low Tide"))),
)

print(ocean_depth(ocean))
print(ocean_depth(tidal_zones))
