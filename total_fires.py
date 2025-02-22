def get_total_fires():
    firesByState = [
        {"year": 2000, "state": "Rio", "month": "Novembro", "number": 18},
        {"year": 2002, "state": "Pernambuco", "month": "Fevereiro", "number": 64},
        {"year": 2001, "state": "Mato Grosso", "month": "Maio", "number": 112},
        {"year": 2003, "state": "Roraima", "month": "Janeiro", "number": 547},
        {"year": 2002, "state": "Maranhao", "month": "Julho", "number": 4},
        {"year": 2003, "state": "Rio", "month": "Março", "number": 9},
        {"year": 2000, "state": "Roraima", "month": "Outubro", "number": 25},
        {"year": 2001, "state": "Paraiba", "month": "Janeiro", "number": 11},
    ]

    firesByYear = [
        {"year": 2002, "number": 68},
        {"year": 2000, "number": 43},
        {"year": 2003, "number": 556},
        {"year": 2001, "number": 123},
    ]

    # for fire_year in firesByYear:
    #     current_sum = 0
    #     for fire_state in firesByState:
    #         if fire_state.get("year") == fire_year["year"]:
    #             current_sum += fire_state["number"]

    #     if current_sum != fire_year["number"]:
    #         return False

    # return True

    state_fires = {}

    for state_fire in firesByState:
        curr_year = state_fire.get("year")
        curr_number = state_fire.get("number")
        state_fires[curr_year] = state_fires.get(curr_year, 0) + curr_number

    for fire in firesByYear:
        year = fire.get("year")
        number = fire.get("number")
        if state_fires.get(year, 0) != number:
            return False

    return True


print(get_total_fires())
