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
