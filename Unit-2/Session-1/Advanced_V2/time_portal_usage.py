"""
In your time travel adventures, you have been collecting data on the usage of different time portals by various travelers. The data is represented by an array usage_records, where usage_records[i] = [traveler_name, portal_number, time_used] indicates that the traveler traveler_name used the portal portal_number at the time time_used.

Return the adventure's "display table". The "display table" is a table whose row entries denote how many times each portal was used at each specific time. The first column is the portal number and the remaining columns correspond to each unique time in chronological order. The first row should be a header whose first column is "Portal", followed by the times in chronological order. Note that the traveler names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.
"""


def display_time_portal_usage(usage_records):
    # Step 1: Extract unique portals and times
    portal_set = set()
    time_set = set()

    for record in usage_records:
        _, portal_number, time_used = record
        portal_set.add(portal_number)
        time_set.add(time_used)

    # Step 2: Prepare the table structure
    portal_list = sorted(portal_set)  # Sorted list of portals
    time_list = sorted(time_set)  # Sorted list of times

    # Initialize a dictionary to hold counts
    usage_count = {portal: {time: 0 for time in time_list} for portal in portal_list}

    # Step 3: Populate the usage count
    for record in usage_records:
        _, portal_number, time_used = record
        usage_count[portal_number][time_used] += 1

    # Step 4: Prepare the output table
    display_table = [["Portal"] + time_list]  # Header row

    for portal in portal_list:
        row = [portal]
        for time in time_list:
            row.append(
                usage_count[portal][time]
            )  # Get the usage count for this portal and time
        display_table.append(row)

    return display_table


usage_records1 = [
    ["David", "3", "10:00"],
    ["Corina", "10", "10:15"],
    ["David", "3", "10:30"],
    ["Carla", "5", "11:00"],
    ["Carla", "5", "10:00"],
    ["Rous", "3", "10:00"],
]
usage_records2 = [
    ["James", "12", "11:00"],
    ["Ratesh", "12", "11:00"],
    ["Amadeus", "12", "11:00"],
    ["Adam", "1", "09:00"],
    ["Brianna", "1", "09:00"],
]
usage_records3 = [
    ["Laura", "2", "08:00"],
    ["Jhon", "2", "08:15"],
    ["Melissa", "2", "08:30"],
]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))
