"""
Write a function a function up_and_down() that accepts a list of integers lst as a parameter. The function should return the number of odd numbers minus the number of even numbers in the list.
"""


def up_and_down(lst):
    """
    P: Find the difference between the number of odd numbers and even numbers in lst

    [1,1,3,4] -> 3 - 1 -> 2
    [1, 2, 4] -> -1

    S: 1. Create counters for both odd and even numbers
    2. Loop through list
    3. Update counter if odd or even
    4. Return difference between counters
    """
    odd_count = 0
    even_count = 0

    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count - even_count


if __name__ == "__main__":
    print(up_and_down([1, 2, 3]))
    print(up_and_down([1, 3, 5]))
    print(up_and_down([2, 4, 10, 2]))
