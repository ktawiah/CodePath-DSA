from collections import defaultdict
from heapq import heappop, heappush


def process_logs(logs):
    inventory = defaultdict(list)
    revenues = []

    for log in logs:
        if log[0] == "supply":
            heappush(inventory[log[1]], (int(log[3]), int(log[2])))

        elif log[0] == "sell":
            robot, count, revenue = log[1], int(log[2]), 0
            while count > 0:
                price, qty = heappop(inventory[robot])
                sell_qty = min(count, qty)
                revenue += sell_qty * price
                count -= sell_qty
                if qty > sell_qty:
                    heappush(inventory[robot], (price, qty - sell_qty))
            revenues.append(revenue)

        elif log[0] == "upgrade":
            robot, count, old_price, new_price = (
                log[1],
                int(log[2]),
                int(log[3]),
                int(log[4]),
            )
            temp = []
            while count > 0:
                price, qty = heappop(inventory[robot])
                if price == old_price:
                    upgrade_qty = min(count, qty)
                    heappush(inventory[robot], (new_price, upgrade_qty))
                    count -= upgrade_qty
                    qty -= upgrade_qty
                if qty > 0:
                    temp.append((price, qty))
            for item in temp:
                heappush(inventory[robot], item)

    return revenues


# Example usage:
logs = [
    ["supply", "robot1", "2", "100"],
    ["supply", "robot2", "3", "60"],
    ["sell", "robot1", "1"],
    ["sell", "robot2", "1"],
    ["upgrade", "robot2", "1", "60", "100"],
    ["sell", "robot2", "1"],
    ["sell", "robot2", "1"],
]

print(process_logs(logs))  # Expected output: [100, 60, 100, 100]
