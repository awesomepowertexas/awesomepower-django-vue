name = "Express Energy"
ptc_name = "Express Energy"
start_texts = ["These average prices"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [[0, tdu_rate + numbers[1] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, 0],
        [500, -500 * numbers[2] / 100 + numbers[6]],
        [1001, -500 * numbers[2] / 100 + 1000 * numbers[9] / 100],
    ]
    rate_function = [[0, numbers[2] / 100], [500, 0], [1001, numbers[9] / 100]]
    return (charge_function, rate_function)


def c(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[1]], [1001, numbers[1] + numbers[3]]]
    rate_function = [[0, 0], [1001, numbers[5] / 100]]
    return (charge_function, rate_function)
