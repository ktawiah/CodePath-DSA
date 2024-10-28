"""
You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.

Return the combined audience size of all performances in audiences with the maximum audience size.

The audience size of a performance is the number of people who attended that performance.

"""


def max_audience_performances(audiences):
    # Create a dictionary to store count of performance numbers
    performance_count = {}

    # Update count dictionary with audiences and count
    for audience in audiences:
        performance_count[audience] = performance_count.get(audience, 0) + 1

    # Get max performance
    max_audiences = max(performance_count.keys())

    # Return multiple of max performance and count
    return max_audiences * performance_count.get(max_audiences)


audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
