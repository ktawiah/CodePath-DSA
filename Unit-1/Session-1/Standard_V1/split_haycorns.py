def split_haycorns(quantity):
    """
    P: Return a list of all the divisors of quantity

    6 -> [1,2,3,6]
    [1] -> [1]
    [3] -> [1,3]

    S: 1. Create a list to store divisors
    2. Loop from 1, to quantity/2
    3. If quantity is divisible by number
    add to list else do nothing
    4. Return list
    """
    splits = []
    for divisor in range(1, int(quantity / 2) + 1):
        if quantity % divisor == 0:
            splits.append(divisor)
    splits.append(quantity)
    return splits


if __name__ == "__main__":
    print(split_haycorns(6))
    print(split_haycorns(3))
    print(split_haycorns(1))
