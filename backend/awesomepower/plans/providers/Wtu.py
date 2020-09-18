name = "WTU Retail Energy"
ptc_name = "WTU RETAIL ENERGY"
start_texts = ["Your actual average price"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
