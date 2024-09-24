def get_last(items):
    """
    P: Returns last element in list else None

    [1,3,4] -> 4
    [] -> None
    [1] -> 1
    """
    if len(items) == 0:
        return None
    else:
        return items[-1]


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
