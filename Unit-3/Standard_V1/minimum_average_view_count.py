"""You manage a collection of view counts for different shows on a streaming platform. You are given an array view_counts of n integers, where n is even.

You repeat the following procedure n / 2 times:

Remove the show with the smallest view count, min_view_count, and the show with the largest view count, max_view_count, from view_counts.
Add (min_view_count + max_view_count) / 2 to the list of average view counts average_views.
Return the minimum element in average_views."""


def minimum_average_view_count(view_counts):
    view_counts.sort()
    # min_avg = float("inf")
    avg_views = []

    while view_counts:
        avg_views.append(((view_counts.pop(0) + view_counts.pop()) / 2))

    return min(avg_views)


print(minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1]))
print(minimum_average_view_count([1, 9, 8, 3, 10, 5]))
print(minimum_average_view_count([1, 2, 3, 7, 8, 9]))
