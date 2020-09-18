name = "Green Energy Exchange"
ptc_name = "GREEN ENERGY EXCHANGE"
start_texts = ["The Average price above"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
