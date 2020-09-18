name = "Spark Energy"
ptc_name = "SPARK ENERGY LLC"
start_texts = ["This estimated average"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[1]]]
    rate_function = [[0, 0], [2000, numbers[0] / 100]]
    return (charge_function, rate_function)


def c(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge], [1000, tdu_charge - numbers[7]]]
    rate_function = [[0, tdu_rate + numbers[0] / 100]]
    return (charge_function, rate_function)
