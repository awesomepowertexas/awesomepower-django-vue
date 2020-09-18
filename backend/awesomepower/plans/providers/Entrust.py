name = "Entrust Energy"
ptc_name = "ENTRUST ENERGY INC"
start_texts = ["This price disclosure"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [[0, tdu_rate + numbers[1] / 100]]
    return (charge_function, rate_function)
