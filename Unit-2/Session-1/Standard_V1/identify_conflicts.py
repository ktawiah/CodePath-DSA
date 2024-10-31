"""
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. Return a dictionary containing the key-value pairs that are the same in each schedule.
"""


def identify_conflicts(venue1_schedule, venue2_schedule):
    dup_schedule = {}
    venue1_artists = set(venue1_schedule.keys())

    for artist, venue in venue2_schedule.items():
        if artist in venue1_artists and venue1_schedule.get(artist) == venue:
            dup_schedule[artist] = venue

    return dup_schedule


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM",
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM",
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
