def highest_altitude(gain):
    """
    P: Determine the net gain as batman moves across each point(basically the sum of all the gains at each point) or return zero if there is a negative result altitude.

    [1,2,3,-4] -> 2
    [-5,1,5,0,-7] -> 0
    """
    sum = 0

    for alt in gain:
        sum += alt
        highest_altitude = max(sum, alt)

    print(highest_altitude)


gain = [-5, 1, 5, 0, -7]
highest_altitude(gain)

gain = [-4, -3, -2, -1, 4, 3, 2]
highest_altitude(gain)
