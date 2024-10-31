"""
Christopher Robin is helping Pooh construct the biggest hunny jar possible. Help his write a function that accepts an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most honey.

Return the maximum amount of honey a container can store.

Notice that you may not slant the container.
"""


def most_honey(height):
    # Create a placeholder for max area
    max_area = 0

    # Create two pointers
    left, right = 0, len(height) - 1

    # Iterate through heights
    while left < right:

        # Get current height
        curr_area = min(height[left], height[right]) * (right - left)

        # Update max height
        max_area = max(curr_area, max_area)

        # Update pointers
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    # Return max area
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))
