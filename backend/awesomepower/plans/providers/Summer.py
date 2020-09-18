name = "Summer Energy"
ptc_name = "SUMMER ENERGY LLC"
start_texts = ["Price Disclosure"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, numbers[10] + numbers[12] + numbers[13]],
        [1000, numbers[10] + numbers[12]],
    ]
    rate_function = [[0, numbers[5] / 100]]
    return (charge_function, rate_function)


def a1(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, numbers[9] + numbers[11] + numbers[12]],
        [1000, numbers[9] + numbers[11]],
    ]
    rate_function = [[0, numbers[4] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[10] + numbers[11]], [1000, numbers[10]]]
    rate_function = [[0, numbers[5] / 100]]
    return (charge_function, rate_function)


def b1(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[9] + numbers[10]], [1000, numbers[9]]]
    rate_function = [[0, numbers[4] / 100]]
    return (charge_function, rate_function)
