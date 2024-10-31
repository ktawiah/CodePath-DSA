"""
You've spent your last few trips exploring different periods of Ancient Greece. During your
travels, you discover several interesting artifacts. Some artifacts appear in multiple
time periods, while others in just one.

You are given two lists of strings artifacts1 and artifacts2 representing the artifacts
found in two different time periods. Write a function find_common_artifacts() that returns
a list of artifacts common to both time periods.

"""

def find_common_artifacts(artifacts1, artifacts2):
    """
    P: Returning the common artifacts between time periods
    """
    
    # Create result list
    result = []
    
    # Convert one artifact to set
    artifacts1_set = set(artifacts1)

    # Iterate through the other aritfact
    for artifact in artifacts2:
        
        # Update result list with common artifact found
        if artifact in artifacts1_set:
            result.append(artifact)

    # Return result list
    return result

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))
