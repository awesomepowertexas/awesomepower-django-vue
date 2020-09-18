name = "MidAmerican Energy Services"
ptc_name = "MIDAMERICAN ENERGY SERVICES LLC"
start_texts = ["The average price"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def a1(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[2] / 100]]
    return (charge_function, rate_function)
