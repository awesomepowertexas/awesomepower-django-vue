name = "V247 Power"
ptc_name = "V247 POWER CORPORATION"
start_texts = ["Fixed Energy Rate"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]], [1001, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
