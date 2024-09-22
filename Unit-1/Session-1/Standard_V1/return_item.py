def get_item(items, x):
    """
    Problem: Return value at a particular index
    Steps:
    1. Use square index notation to get item in list if item exists or None if item does not
    2. Return item
    """
    return items[x] if x < len(items) else None


if __name__ == "__main__":

    print(get_item(["piglet", "pooh", "roo", "rabbit"], 2))
    print(get_item(["piglet", "pooh", "roo", "rabbit"], 5))
