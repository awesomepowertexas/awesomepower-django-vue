name = "PowerNext"
ptc_name = "PowerNext"
start_texts = ["The average price above"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[1]]]
    rate_function = [[0, numbers[0] / 100]]
    return (charge_function, rate_function)


def a1(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[1] - numbers[2]]]
    rate_function = [[0, numbers[0] / 100 - numbers[3]]]
    return (charge_function, rate_function)
