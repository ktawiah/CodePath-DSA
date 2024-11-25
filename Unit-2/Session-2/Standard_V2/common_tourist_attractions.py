"""Given two lists of tourist attractions, tourist_list1 and tourist_list2, find the common attractions with the least total travel time.

A common attraction is one that appears in both tourist_list1 and tourist_list2.

A common attraction with the least total travel time is a common attraction such that if it appeared at tourist_list1[i]
and tourist_list2[j] then i + j should be the minimum value among all the other common attractions.

Return all the common attractions with the least total travel time. Return the answer in any order.
"""


def find_attractions(tourist_list1, tourist_list2):
    pass


tourist_list1 = ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"]
tourist_list2 = ["Colosseum", "Trevi Fountain", "Pantheon", "Eiffel Tower"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"]
tourist_list2 = ["Disneyland", "Eiffel Tower", "Notre-Dame"]

print(find_attractions(tourist_list1, tourist_list2))

tourist_list1 = ["beach", "mountain", "forest"]
tourist_list2 = ["mountain", "beach", "forest"]

print(find_attractions(tourist_list1, tourist_list2))
