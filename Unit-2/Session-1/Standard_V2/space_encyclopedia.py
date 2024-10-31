"""
Given a dictionary planets that maps planet names to a dictionary containing the planet's number of moons and orbital period, write a function planet_lookup() that accepts a string planet_name and returns a string in the form Planet <planet_name> has an orbital period of <orbital period> Earth days and has <number of moons> moons. If planet_name is not a key in planets, return "Sorry, I have no data on that planet.".
"""


def planet_lookup(planets, planet_name):
    # Check if in planets
    if planet_name not in planets:
        return f"Sorry, I have no data on {planet_name}"
    # Look-up orbital and number of moons of given planet
    moons = planets.get(planet_name).get("Moons")
    orbits = planets.get(planet_name).get("Orbital Period")

    # Return formatted string
    return f"Planet {orbits} has an orbital period of {orbits} Earth days and has {moons} moons."


planetary_info = {
    "Mercury": {"Moons": 0, "Orbital Period": 88},
    "Earth": {"Moons": 1, "Orbital Period": 365.25},
    "Mars": {"Moons": 2, "Orbital Period": 687},
    "Jupiter": {"Moons": 79, "Orbital Period": 10592},
}

print(planet_lookup(planetary_info, "Jupiter"))
print(planet_lookup(planetary_info, "Pluto"))
