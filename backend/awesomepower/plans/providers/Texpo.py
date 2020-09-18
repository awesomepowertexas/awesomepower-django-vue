name = "Texpo Energy"
ptc_name = "TEXPO ENERGY"
start_texts = ["Thank you for choosing"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]], [1000, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
