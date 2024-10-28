"""
Write a function data_difference() that accepts two dictionaries experiment1 and experiment2 and returns a new dictionary that contains only key-value pairs found exclusively in experiment1 but not in experiment2.
"""


def data_difference(experiment1, experiment2):
    # Create new map to store unique experiments
    unique_experiments = {}

    # Iterate through experiment1
    for experiment, result in experiment1.items():

        # Add experiment to new map if not in experiment 2
        if result != experiment2.get(experiment):
            unique_experiments[experiment] = result

    # Return unique experiments
    return unique_experiments


exp1_data = {"temperature": 22, "pressure": 101.3, "humidity": 45}
exp2_data = {"temperature": 18, "pressure": 101.3, "radiation": 0.5}

print(data_difference(exp1_data, exp2_data))
