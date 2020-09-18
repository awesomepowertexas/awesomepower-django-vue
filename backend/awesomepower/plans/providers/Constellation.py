name = "Constellation NewEnergy"
ptc_name = "CONSTELLATION NEWENERGY INC"
start_texts = ["This estimated average"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[2]], [1000, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge],
        [1000, tdu_charge - numbers[4]],
        [2000, tdu_charge - numbers[4] - numbers[6]],
    ]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def c(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, numbers[2]],
        [501, numbers[2] + numbers[5]],
        [1001, numbers[2] + numbers[5] + numbers[8]],
        [1501, numbers[2] + numbers[5] + numbers[8] + numbers[11]],
    ]
    rate_function = [[0, 0], [2001, numbers[13] / 100]]
    return (charge_function, rate_function)
