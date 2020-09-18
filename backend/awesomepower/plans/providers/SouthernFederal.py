name = "Southern Federal Power"
ptc_name = "SOUTHERN FEDERAL POWER LLC"
start_texts = ["Your monthly electric bill"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[1]]]
    rate_function = [[0, tdu_rate + numbers[0]]]
    return (charge_function, rate_function)
