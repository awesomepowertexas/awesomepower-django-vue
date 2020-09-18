name = "Infinite Energy"
ptc_name = "INFINITE ENERGY"
start_texts = ["Infinite Energy charges"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]], [1000, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[9]]]
    rate_function = [[0, 0], [1001, numbers[8] / 100]]
    return (charge_function, rate_function)
