name = "Windrose Energy"
ptc_name = "WINDROSE ENERGY"
start_texts = ["The above price"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [[0, tdu_rate + numbers[1] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[0]]]
    rate_function = [[0, numbers[1] / 100]]
    return (charge_function, rate_function)
