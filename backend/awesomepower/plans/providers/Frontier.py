name = "Frontier Utilities"
ptc_name = "FRONTIER UTILITIES"
start_texts = ["The above price disclosure"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
