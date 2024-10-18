"""
Christopher Robin is helping Pooh construct the biggest hunny jar possible. Help his write a function that accepts an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most honey.

Return the maximum amount of honey a container can store.

Notice that you may not slant the container.
"""


def most_honey(height):
    # Create volume placeholder
    # For each pair check if max volume
    # If max store indices
    # Return square of min index

    max_volume = 0

    for idx1, num1 in enumerate(height):
        for idx2, num2 in enumerate(height):
            # print(idx1, idx2, (idx2 - idx1) * min(num1, num2))
            if (idx2 - idx1) * min(num1, num2) > max_volume:
                max_volume = (idx2 - idx1) * min(num1, num2)
                height1 = idx1
                height2 = idx2

    print(min(height[height1], height[height2]) ** 2)


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)
