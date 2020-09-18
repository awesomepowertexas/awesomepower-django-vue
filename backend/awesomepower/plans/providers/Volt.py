name = "Volt Electricity"
ptc_name = "VOLT ELECTRICITY PROVIDER LP"
start_texts = ["Volt Energy Charge"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[8] / 100]]
    return (charge_function, rate_function)


def a1(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
