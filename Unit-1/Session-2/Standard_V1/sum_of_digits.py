def sum_of_digits(num):
    """
    P: Return the sum of digits in integer, num

    132 -> 6
    98 -> 17

    S: 1. Create placeholder for sum and initialize to 0
    2. While num is not equal to 0,
         - Add num % 10 to sum
         - assign num to num // 10 - floor division
    3. Return sum
    """
    digit_sum = 0

    while num != 0:
        digit_sum += num % 10
        num //= 10

    return digit_sum


if __name__ == "__main__":
    print(sum_of_digits(423))
    print(sum_of_digits(132))
    print(sum_of_digits(98))
