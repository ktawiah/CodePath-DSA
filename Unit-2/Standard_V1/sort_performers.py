"""
You are given an array of strings performer_names, and an array performance_times that consists of distinct positive integers representing the performance durations in minutes. Both arrays are of length n.

For each index i, performer_names[i] and performance_times[i] denote the name and performance duration of the ith performer.

Return performer_names sorted in descending order by the performance durations.
"""


def sort_performers(performer_names, performance_times):
    """
    :type performer_names: List[str]
    :type performance_times: List[int]
    :rtype: List[str]
    """

    # Create performer_duration map
    duration_performer = {}

    for index in range(len(performer_names)):
        duration_performer[performance_times[index]] = performer_names[index]

    # Sort dictionary by durations
    sorted_durations = sorted(duration_performer.keys(), reverse=True)

    # Create result list
    result = []

    for duration in sorted_durations:
        result.append(duration_performer.get(duration))

    # Return keys(performers) after sorting
    return result


performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1))
print(sort_performers(performer_names2, performance_times2))
