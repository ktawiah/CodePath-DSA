"""In a pet adoption center, there are two groups of volunteers: the "Cat Lovers" and the "Dog Lovers."

The center is deciding on which type of pet should be receive extra treats that week, and the voting takes place in a round-based procedure. In each round, each volunteer can exercise one of the two rights:

Ban one volunteer's vote: A volunteer can make another volunteer from the opposite group lose all their rights in this and all the following rounds.
Announce the victory: If a volunteer finds that all the remaining volunteers with the right to vote are from the same group, they can announce the victory for their group and prioritize their preferred pet for extra treats.
Given a string votes representing each volunteer's group affiliation. The character 'C' represents "Cat Lovers" and 'D' represents "Dog Lovers". The length of the given string represents the number of volunteers.

Predict which group will finally announce the victory and prioritize their preferred pet for extra treats. The output should be "Cat Lovers" or "Dog Lovers".
"""

from collections import deque


def predictAdoption_victory(votes):
    dog_queue, cat_queue = deque(), deque()

    for i, vote in enumerate(votes):
        if vote == "C":
            cat_queue.append(i)
        else:
            dog_queue.append(i)

    while cat_queue and dog_queue:
        cat_vote, dog_vote = cat_queue.popleft(), dog_queue.popleft()

        if cat_vote < dog_vote:
            cat_queue.append(cat_vote)
        else:
            dog_queue.append(dog_vote)

    return "Cat Lovers" if cat_queue else "Dog Lovers"


print(predictAdoption_victory("CD"))
print(predictAdoption_victory("CDD"))
