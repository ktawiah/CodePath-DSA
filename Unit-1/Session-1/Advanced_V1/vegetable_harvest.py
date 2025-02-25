"""
Rabbit is collecting carrots from his garden to make a feast for Pooh and friends. Write a function harvest() that accepts a 2D n x m matrix vegetable_patch and returns the number of of carrots that are ready to harvest in the vegetable patch. A carrot is ready to harvest sif vegetable_patch[i][j] has value 'c'.

Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.
"""


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
