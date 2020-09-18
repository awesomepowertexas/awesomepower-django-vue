name = "Veteran Energy"
ptc_name = "VETERAN ENERGY LLC"
start_texts = ["Your Average Price"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]], [1000, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
