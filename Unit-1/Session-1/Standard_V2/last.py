"""
Implement a function get_last() that accepts a list of items items and returns the last item in the list. If the list is empty, return None.
"""


def get_last(items):
    """
    P: Returns last element in list else None

    [1,3,4] -> 4
    [] -> None
    [1] -> 1
    """
    # if len(items) == 0:
    #     return None
    # else:
    #     return items[-1]

    return items.pop() if len(items) != 0 else None


if __name__ == "__main__":
    print(
        get_last(
            [
                "spider man",
                "batman",
                "superman",
                "iron man",
                "wonder woman",
                "black adam",
            ]
        )
    )
    print(get_last([]))
