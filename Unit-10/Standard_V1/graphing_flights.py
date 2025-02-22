"""As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of a different destination and flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i]. Write a function bidirectional_flights() that returns True if for any flight from a destination i to a destination j there also exists a flight from destination j to destination i. Return False otherwise.
"""


def bidirectional_flights(flights):
    for index, dest_list in enumerate(flights):
        for dest in dest_list:
            if index not in flights[dest]:
                return False

    return True


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))

# True
# False
