"""
Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, return the number of popular song pairs.

A pair (i, j) is called popular if the songs have the same popularity score and i < j.

Hint: number of pairs = (n x n-1)/2
"""


def num_popular_pairs(popularity_scores):
    # Create placeholder for sum
    score_sum = 0

    # Determine the count of each score
    score_count = {}
    for score in popularity_scores:
        score_count[score] = score_count.get(score, 0) + 1

    # Iterate through score counts
    for score, count in score_count.items():

        # Add combination of score to sum if score > 0, else do nothing
        if score > 0:
            score_sum += (count * (count - 1)) // 2

    # Return sum
    return score_sum


popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3))
