"""
Write a function which takes in two polynomial functions and returns the product of the functions.
"""


def get_polynomial(pol_number: str):
    number_of_terms = int(input(f"Enter number of terms in {pol_number} polynomial: "))

    degree_coefficient = {}

    term_number = 1

    while number_of_terms:
        degree = int(input(f"Enter the degree for term number {term_number}: "))
        coefficient = float(
            input(
                f"Enter the coefficient for term number {term_number} NB:Input decimal value if fraction: "
            )
        )
        if degree in degree_coefficient:
            print(f"Term of degree {degree} has already been entered. Enter another")
            term_number -= 1
            number_of_terms += 1
        else:
            degree_coefficient[degree] = coefficient

        term_number += 1
        number_of_terms -= 1

    return degree_coefficient


def convert_to_pol_string(pol_map):
    result = []
    for degree, coefficient in pol_map.items():
        result.append(f"{coefficient}x^{degree}")

    return " + ".join(result)


def multiply_polynomials():
    first_polynomial, second_polynomial = get_polynomial("first"), get_polynomial(
        "second"
    )

    result_map = {}

    for f_degree, f_coefficient in first_polynomial.items():
        for s_degree, s_coefficient in second_polynomial.items():
            new_degree, new_coefficient = (
                f_degree + s_degree,
                f_coefficient * s_coefficient,
            )

            if new_degree in result_map:
                result_map[new_degree] += new_coefficient
            else:
                result_map[new_degree] = new_coefficient

    return convert_to_pol_string(result_map)


if __name__ == "__main__":
    print(multiply_polynomials())
