def longestSubarrayWithSumK(a, k):
    # Create placeholders for start, end, max_len, and window sum
    start, end = 0, 0
    max_length = float("-inf")
    window_sum = 0

    # Iterate through list
    while end < len(a):

        # Update window sum
        window_sum += a[end]

        # Shrink window until sum == k
        while window_sum > k:
            window_sum -= a[start]
            start += 1

        # Update max if sum == k
        if window_sum == k:
            max_length = max(max_length, end - start + 1)

        end += 1

    # Return max
    return max_length
