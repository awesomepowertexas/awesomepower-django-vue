name = "Eligo Energy"
ptc_name = "ELIGO ENERGY TX LLC"
start_texts = ["The price you pay"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [[0, tdu_rate + numbers[1] / 100]]
    return (charge_function, rate_function)
