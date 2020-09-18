name = "Infuse Energy"
ptc_name = "INFUSE ENERGY LLC"
start_texts = ["ENERGY CHARGES"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[3]],
        [500, tdu_charge],
        [1000, tdu_charge - numbers[7]],
        [1501, tdu_charge - numbers[12]],
    ]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
