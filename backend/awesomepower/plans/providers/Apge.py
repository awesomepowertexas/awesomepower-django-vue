name = "AP Gas & Electric"
ptc_name = "AP GAS & ELECTRIC (TX) LLC"
start_texts = ["Your actual average price"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
