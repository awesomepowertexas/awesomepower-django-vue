name = "Champion Energy"
ptc_name = "CHAMPION ENERGY SERVICES LLC"
start_texts = ["This price disclosure", "The average price per"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
