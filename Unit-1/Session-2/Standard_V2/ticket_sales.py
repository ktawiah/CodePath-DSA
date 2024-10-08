def total_sales(ticket_sales):
    ticket_sum = 0

    for sale in ticket_sales.values():
        ticket_sum += sale

    return ticket_sum


ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
