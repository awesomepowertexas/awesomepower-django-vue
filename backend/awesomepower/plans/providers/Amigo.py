name = "Amigo Energy"
ptc_name = "AMIGO ENERGY"
start_texts = ["This price disclosure"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[1]]]
    rate_function = [[0, numbers[0] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, 0]]
    rate_function = [[0, numbers[0] / 100]]
    return (charge_function, rate_function)
