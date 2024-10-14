"""
The legendary outlaw Robin Hood is looking for the target of his next heist. Write a function wealthiest_customer() that accepts an m x n 2D integer matrix accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return a list [i, w] where i is the 0-based index of the wealthiest customer and w is the total wealth of the wealthiest customer.

If multiple customers have the highest wealth, return the index of any customer.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""


def wealthiest_customer(accounts):
    # Create a map to store index, wealth pairs
    wealth_map = {}

    # Iterate through accounts and update map
    for row_idx, row_value in enumerate(accounts):
        for col_idx, col_value in enumerate(row_value):
            wealth_map[row_idx] = (
                wealth_map.get(row_idx, 0) + accounts[row_idx][col_idx]
            )

    # Iterate through map to determine max wealth
    result_list = [0, 0]
    for index, wealth in wealth_map.items():
        if wealth > result_list[1]:
            result_list[1] = wealth
            result_list[0] = index

    print(result_list)


accounts = [[1, 2, 3], [3, 2, 1]]
wealthiest_customer(accounts)

accounts = [[1, 5], [7, 3], [3, 5]]
wealthiest_customer(accounts)

accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
wealthiest_customer(accounts)
