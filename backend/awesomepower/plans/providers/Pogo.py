name = "Pogo Energy"
ptc_name = "Pogo Energy"
start_texts = ["Average Price per kWh above"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1] * 30]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def a1(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[2] * 30]]
    rate_function = [[0, tdu_rate + numbers[1] / 100]]
    return (charge_function, rate_function)
