"""
In your time travel adventures, you are given an integer array anomalies where anomalies[i] = [traveleri, anomalyi] indicates that the traveler traveleri caused a temporal anomaly anomalyi.

Return a list answer of size 2 where:

answer[0] is a list of all travelers that have not caused any anomalies.
answer[1] is a list of all travelers that have caused exactly one anomaly.
The values in the two lists should be returned in increasing order.

Note: You should only consider the travelers that have experienced at least one anomaly.
"""


def find_travelers(anomalies):
    # Create two hash maps to keep track of counts of both travelers and anomalies
    travelers_map = {}
    anomalies_map = {}

    for traveler, anomaly in anomalies:
        travelers_map[traveler] = travelers_map.get(traveler, 0) + 1

        anomalies_map[anomaly] = anomalies_map.get(anomaly, 0) + 1

    # Create ro_anomalies list
    zero_anomalies = []

    # Create one anomalies list
    one_anomalies = []

    # Iterate through travelers and anomalies independently and update both lists
    for traveler in travelers_map.keys():
        if traveler not in anomalies_map:
            zero_anomalies.append(traveler)

    for key, value in anomalies_map.items():
        if value == 1:
            one_anomalies.append(key)

    # Sort anomaly lists
    zero_anomalies.sort()
    one_anomalies.sort()
    # Return matrix
    return [zero_anomalies, one_anomalies]


anomalies1 = [
    [1, 3],
    [2, 3],
    [3, 6],
    [5, 6],
    [5, 7],
    [4, 5],
    [4, 8],
    [4, 9],
    [10, 4],
    [10, 9],
]
anomalies2 = [[2, 3], [1, 3], [5, 4], [6, 4]]

print(find_travelers(anomalies1))
print(find_travelers(anomalies2))
