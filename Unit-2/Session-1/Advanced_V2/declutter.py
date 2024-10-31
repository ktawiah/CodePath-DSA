"""
As a time traveler, you've collected a mountain of souvenirs over the course of your travels.
You're running out of room to store them all and need to declutter. Given a list of strings
souvenirs and a integer threshold, declutter your souvenirs by writing a function declutter()
that returns a list of souvenirs strictly below threshold.
"""

def declutter(souvenirs, threshold):
    """
    P: Return list of souvenirs whose number is below given threshold
    """

    # Create a freq map to store souvenir counts
    souvenir_count = {}
    for souvenir in souvenirs:
        souvenir_count[souvenir] = souvenir_count.get(souvenir, 0) + 1

    # Create result list
    result = []

    # Iterate through map
    for souvenir, count in souvenir_count.items():
        
        # Update result list based on count
        if count < threshold:
            while count != 0:
                result.append(souvenir)
                count -= 1
    
    # Return result list
    return result

souvenirs = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold = 3
print(declutter(souvenirs, threshold))

souvenirs = ["postcard", "postcard", "postcard", "sword"]
threshold = 2

print(declutter(souvenirs, threshold))
