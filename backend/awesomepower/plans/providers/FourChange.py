name = "4Change Energy"
ptc_name = "4CHANGE ENERGY"
start_texts = ["This price disclosure"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [[0, tdu_rate + numbers[1] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[1]], [1001, numbers[1] + numbers[3]]]
    rate_function = [[0, 0], [2000, numbers[5] / 100]]
    return (charge_function, rate_function)
