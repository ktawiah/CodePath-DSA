"""
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id numbers to the artist they voted for, return the artist that had the most number of votes. If there is a tie, return any artist with the top number of votes.
"""


def best_set(votes):
    artist_votes = {}

    for artist in votes.values():
        artist_votes[artist] = artist_votes.get(artist, 0) + 1

    max_votes = 0
    # best_artist = ""
    print(artist_votes)

    for curr_artist, vote in artist_votes.items():
        if vote > max_votes:
            max_votes = vote
            best_artist = curr_artist

    return best_artist


votes1 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA",
}

votes2 = {
    1234: "SZA",
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
}

print(best_set(votes1))
print(best_set(votes2))
