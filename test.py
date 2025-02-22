def getminNumberOfSwaps(arr):
    """
    Problem: Given an array of binary digits, rearrange the array such that all the zeros
    are grouped at one end and all the ones are grouped at the opposite end. Calculate
    the minimum number of swaps needed to sort the array in this manner.

    Approach-1:
    1. A brute-force approach would try every possible configuration and count the swaps.
    2. This is inefficient and would not work well for larger arrays, since the time complexity
       would be high.

    Approach-2 (Optimal Solution):
    1. Count the total number of 1s in the array. Let's call this count "total_ones".
    2. Use a sliding window of size "total_ones" and count how many 1s are in each window.
    3. The minimum number of swaps needed is the window with the fewest 1s, which corresponds to
       the fewest out-of-place 1s.
    4. This will give the number of swaps required to move all 1s together and all 0s together.

    Time Complexity: O(n), since we just go over the array once to count the 1s and then slide the window.
    Space Complexity: O(1), we only need a few extra variables.

    Solve -> Done
    Step -> Done
    """
    min_zero_swaps, min_one_swaps = 0, 0
    one_count, zero_count = 0, 0

    for num in arr:
        if num == 0:
            zero_count += 1
            min_zero_swaps += one_count
        else:
            one_count += 1
            min_one_swaps += zero_count

    return min(min_one_swaps, min_zero_swaps)


print(getminNumberOfSwaps([0, 1, 0, 1]))

# public static int minSwaps(int[] arr) {
#     int min_swaps1 = 0;
#     int zero_counts = 0;
#     int min_swaps2 = 0;
#     int one_counts = 0;

#     for (int j : arr) {
#         if (j == 0) {
#             zero_counts++;
#             min_swaps2 += one_counts;
#         } else {
#             one_counts++;
#             min_swaps1 += zero_counts;
#         }
#     }

#     return Math.min(min_swaps1, min_swaps2);
# }

# # Step 1: Count the total number of 1s in the array
# total_ones = sum(arr)

# # Step 2: If there are no 1s or no 0s, no swaps are needed
# if total_ones == 0 or total_ones == len(arr):
#     return 0

# # Step 3: Use a sliding window of size total_ones
# # to find the minimum number of 1s in any window of size total_ones
# min_swaps = float("inf")
# current_ones_in_window = 0

# # Initialize the first window (first total_ones elements)
# for i in range(total_ones):
#     if arr[i] == 1:
#         current_ones_in_window += 1

# min_swaps = current_ones_in_window

# # Slide the window over the array
# for i in range(total_ones, len(arr)):
#     # Remove the leftmost element of the previous window and add the new element
#     if arr[i - total_ones] == 1:
#         current_ones_in_window -= 1
#     if arr[i] == 1:
#         current_ones_in_window += 1

#     # Track the minimum number of 1s in any window
#     min_swaps = min(min_swaps, current_ones_in_window)

# # Step 4: The result is the minimum number of swaps needed
# return min_swaps


# Sample test case
# arr = [0, 1, 0, 1]
# print(getminNumberOfSwaps(arr))  # Output: 1


# print(getminNumberOfSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]))

# # Given list
# lst = [3, 3, 10, 7, 4, 3, 0]

# # Initialize an empty stack
# stack = []

# # Iterate through each element in the list
# for element in lst:
#     if element % 2 == 1:  # Check if the element is odd
#         stack.append(element)
#     else:  # Element is even
#         if stack:
#             old_element = stack.pop()
#             if old_element > element:
#                 stack.append(element)

# # Print the final state of the stack and the maximum stack size
# print("Final stack:", stack)
# print("Maximum stack size:", len(stack))
