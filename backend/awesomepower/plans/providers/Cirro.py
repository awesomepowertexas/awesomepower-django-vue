name = "Cirro Energy"
ptc_name = "CIRRO ENERGY"
start_texts = ["Energy Charge"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def b1(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, 0]]
    rate_function = [[0, numbers[0] / 100]]
    return (charge_function, rate_function)


def b2(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, 0]]
    rate_function = [[0, numbers[1] / 100]]
    return (charge_function, rate_function)
