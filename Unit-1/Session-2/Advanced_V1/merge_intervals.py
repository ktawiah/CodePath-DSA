"""
Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


def merge_intervals(intervals):
    # Assume that first interval is merged
    merged_list = [intervals[0]]

    # Iterate through intervals
    for interval in intervals:
        # Get last last interval in merged_list
        last_interval = merged_list[-1]

        # Compare current interval with last interval
        if last_interval[1] > interval[0]:
            last_interval[1] = interval[1]
        else:
            merged_list.append(interval)

    print(merged_list)


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
