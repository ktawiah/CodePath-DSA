"""
Write a function trilogy() that accepts an integer year and prints the title of the Batman trilogy movie released that year as outlined below.

Year	Movie Title
2005	"Batman Begins"
2008	"The Dark Knight"
2012	"The Dark Knight Rises"
If the given year does not match one of the years in the table above, print "Christopher Nolan did not release a Batman movie in <year>."
"""


def trilogy(year):
    """
    P: Return a conditional string based on a year input
    """
    trilogy_dict = {
        2005: "Batman Begins",
        2008: "The Dark Knight",
        2012: "The Dark Knight Rises",
    }

    return (
        trilogy_dict.get(year)
        if year in trilogy_dict
        else f"Christopher Nolan did not release a Batman movie in {year}."
    )


if __name__ == "__main__":
    print(trilogy(2008))
    print(trilogy(1998))
