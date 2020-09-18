name = "New Power Texas"
ptc_name = "New Power Texas"
start_texts = ["The average price above"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [1000, tdu_charge + numbers[0] - numbers[2]],
    ]
    rate_function = [[0, tdu_rate + numbers[1]]]
    return (charge_function, rate_function)
