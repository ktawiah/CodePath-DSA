"""
Ground control is analyzing signal patterns received from different probes. You are given a 0-indexed array signals consisting of distinct strings.

The string signals[i] can be paired with the string signals[j] if the string signals[i] is equal to the reversed string of signals[j]. 0 <= i < j < signals.length. Return the maximum number of pairs that can be formed from the array signals.

Note that each string can belong in at most one pair.
"""


def max_number_of_string_pairs(signals):
    """
    P: Return the max count of the pairable signal data

    What if there are more than two pairs?
    """

    # Create a map for count of pairs
    probe_count = {}

    for signal in signals:
        probe_count[signal] = probe_count.get(signal, 0) + 1

    # Create sum acc. for number of pairs
    sum_pairs = 0

    # Iterate through signals
    for signal in signals:

        # Reverse signal
        signal_list = list(signal)
        signal_list.reverse()
        reverse_signal = "".join(signal_list)
        print(reverse_signal)

        # Update sum with value in map
        sum_pairs += probe_count.get(reverse_signal, 0)

    # Return sum
    return sum_pairs


signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]

print(max_number_of_string_pairs(signals1))
print(max_number_of_string_pairs(signals2))
print(max_number_of_string_pairs(signals3))
