"""
NASA has asked the public to vote on a new name for one of the nodes in the International Space Station. Given a list of strings votes where each string in the list is a voter's suggested new name, implement a function get_winner() that returns the suggestion with the most number of votes.

If there is a tie, return either option.
"""


def get_winner(votes):
    """
    P: Return the max frequency of votes
    """

    # Create map to store vote and count
    vote_count = {}

    # Iterate through map
    for vote in votes:
        vote_count[vote] = vote_count.get(vote, 0) + 1

    # Get max votes
    max_votes = 0
    winner = ""

    for vote, count in vote_count.items():
        if count >= max_votes:
            winner = vote
            max_votes = count

    # Return winner
    return winner


votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

print(get_winner(votes1))
print(get_winner(votes2))
