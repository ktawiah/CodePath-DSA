"""In Wakanda, vibranium is the most precious resource, and it is found in several deposits. Each deposit is represented by a character in a string
(e.g., "V" for vibranium, "G" for gold, etc.)

Given a string resources, write a recursive function count_deposits() that returns the total number of distinct vibranium deposits in resources.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""
def count_deposits(resources):
    resources_list = list(resources)

    def helper(resource_list, count=0):
        if len(resource_list)==0:
            return count

        if resource_list.pop() == "V":
            count += 1

        return  helper(resource_list, count)

    return helper(resources_list)

print(count_deposits("VVVVV"))
print(count_deposits("VXVYGA"))