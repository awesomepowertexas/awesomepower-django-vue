name = "Ambit Energy"
ptc_name = "AMBIT ENERGY"
start_texts = ["per month"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [[0, tdu_rate + numbers[1]]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [
        [0, tdu_rate + numbers[5]],
        [501, tdu_rate + numbers[6]],
        [1001, tdu_rate + numbers[7]],
    ]
    return (charge_function, rate_function)
