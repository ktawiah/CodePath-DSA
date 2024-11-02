"""As the activities director on a cruise ship, you’re organizing excursions for the passengers. You have a sorted list of non-negative integers excursion_counts, where each number represents the number of passengers who have signed up for various excursions at your next cruise destination. The list is considered profitable if there exists a number x such that there are exactly x excursions that have at least x passengers signed up.

Write a function that detrmines whether excursion_counts is profitable. If it is profitable, return the value of x. If it is not profitable, return -1. It can be proven that if excursion_counts is profitable, the value for x is unique.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""


def is_profitable(excursion_counts, start=0, count=0):
    if len(excursion_counts) < 1:
        return -1

    if start == len(excursion_counts):
        return count if count > 0 else -1

    if excursion_counts[start] >= len(excursion_counts):
        count += 1

    return is_profitable(excursion_counts, start + 1, count)


print(is_profitable([3, 5]))
print(is_profitable([0, 0]))
