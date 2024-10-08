def harvest(vegetable_patch):
    """
    P: Return the number of carrots which are ready to be harvestes

    [[x, c], [b, c], [d, a], [c, c]] -> 4

    S: 1. Create placeholder of carrot count
    2. Loop through rows and columns (inner loop)
    3. Increment count if cell is equal to c else do nothing
    4. return carrot count
    """
    carrot_count = 0

    for row in vegetable_patch:
        for col in row:
            if col == "c":
                carrot_count += 1

    return carrot_count


vegetable_patch = [["x", "c", "x"], ["x", "x", "x"], ["x", "c", "c"], ["c", "c", "c"]]
print(harvest(vegetable_patch))
