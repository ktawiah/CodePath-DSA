"""
In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), you start your journey at the first observation point (index 0). To make observations in a specific order represented by a string observations, you need to move from one point to another.

The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.

Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.
"""


def navigate_research_station(station_layout, observations):
    # Create placeholder for total time
    total_time = 0

    # Create placeholder for prev pointer
    prev = 0

    # Iterate through observations
    for observation in observations:

        # Iterate through station layout
        for idx2, layout in enumerate(station_layout):

            # Update total time
            if observation == layout:
                total_time += abs(idx2 - prev)
                prev = idx2

    # Return total time
    return total_time


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))
print(navigate_research_station(station_layout2, observations2))
