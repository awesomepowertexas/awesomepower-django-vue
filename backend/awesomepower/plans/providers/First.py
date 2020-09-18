name = "First Choice Power"
ptc_name = "FIRST CHOICE POWER"
start_texts = ["Your actual average price", "Energy Charge"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1] * 30]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
