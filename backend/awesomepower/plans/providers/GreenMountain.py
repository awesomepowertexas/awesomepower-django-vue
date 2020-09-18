name = "Green Mountain Energy"
ptc_name = "GREEN MOUNTAIN ENERGY COMPANY"
start_texts = ["This price disclosure"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [[0, tdu_rate + numbers[1] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [
        [0, tdu_rate + numbers[3] / 100],
        [1001, tdu_rate + numbers[5] / 100],
    ]
    return (charge_function, rate_function)
