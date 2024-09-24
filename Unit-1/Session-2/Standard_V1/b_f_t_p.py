def bouncy_flouncy_trouncy_pouncy(operations):
    """
    P: Return final value of tiger
        bouncy, flouncy -> tiger++
        trouncy, pouncy -> tiger--

    ["pouncy", "flouncy", "pouncy"], t=1 -> 0

    S: 1. Initialize tiger to 1
    2. Store increment or decrement operations in sets
    3. Loop through operations list
    4. If current element in either lists, add or decrement tiger resp.
    5. Return tiger

    """
    tiger = 1
    increment_set = {"bouncy", "flouncy"}

    for operation in operations:
        if operation in increment_set:
            tiger += 1
        else:
            tiger -= 1

    return tiger


if __name__ == "__main__":
    print(bouncy_flouncy_trouncy_pouncy(["trouncy", "flouncy", "flouncy"]))
    print(bouncy_flouncy_trouncy_pouncy(["bouncy", "bouncy", "flouncy"]))
    print(
        bouncy_flouncy_trouncy_pouncy(
            ["pouncy", "flouncy", "pouncy"],
        )
    )
