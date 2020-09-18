name = "Discount Power"
ptc_name = "Discount Power"
start_texts = ["The price you pay"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]], [1000, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[4] / 100]]
    return (charge_function, rate_function)
