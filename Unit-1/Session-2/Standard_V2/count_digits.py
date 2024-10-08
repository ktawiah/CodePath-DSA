def count_digits(n):
    """
    P: Count the number of digits in integer n

    3275 -> 4
    300183 -> 6
    1 -> 1

    S: 1. Create placeholder for digit list
    2. Separate digits into list using % and //
    2. Return length of list
    """
    digits = []

    while n != 0:
        digits.append(n % 10)
        n //= 10

    return len(digits)


if __name__ == "__main__":
    print(count_digits(964))
    print(count_digits(300183))
    print(count_digits(3275))
    print(count_digits(0))
    print(count_digits(1))
