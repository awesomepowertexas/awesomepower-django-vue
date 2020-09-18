name = "Energy to Go"
ptc_name = "Energy to Go"
start_texts = ["The average price above"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, numbers[1]]]
    rate_function = [[0, numbers[0] / 100]]
    return (charge_function, rate_function)
