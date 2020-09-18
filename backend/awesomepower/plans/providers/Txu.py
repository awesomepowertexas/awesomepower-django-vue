name = "TXU Energy"
ptc_name = "TXU ENERGY"
start_texts = ["Your average price"]


def a(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [[0, tdu_rate + numbers[1] / 100]]
    return (charge_function, rate_function)


def a1(numbers, tdu_charge, tdu_rate):
    charge_function = [[0, tdu_charge + numbers[0]]]
    rate_function = [[0, tdu_rate + numbers[2] / 100]]
    return (charge_function, rate_function)


def b(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [1200, tdu_charge + numbers[0] - numbers[10]],
    ]
    rate_function = [
        [0, tdu_rate + numbers[3] / 100],
        [1201, tdu_rate + numbers[6] / 100],
        [2001, tdu_rate + numbers[8] / 100],
    ]
    return (charge_function, rate_function)


def b1(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [1200, tdu_charge + numbers[0] - numbers[12]],
    ]
    rate_function = [
        [0, tdu_rate + numbers[3] / 100],
        [1201, tdu_rate + numbers[6] / 100],
        [2001, tdu_rate + numbers[8] / 100],
    ]
    return (charge_function, rate_function)


def b2(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [1200, tdu_charge + numbers[0] - numbers[11]],
    ]
    rate_function = [
        [0, tdu_rate + numbers[4] / 100],
        [1201, tdu_rate + numbers[7] / 100],
        [2001, tdu_rate + numbers[9] / 100],
    ]
    return (charge_function, rate_function)


def b3(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [1200, tdu_charge + numbers[0] - numbers[13]],
    ]
    rate_function = [
        [0, tdu_rate + numbers[4] / 100],
        [1201, tdu_rate + numbers[7] / 100],
        [2001, tdu_rate + numbers[9] / 100],
    ]
    return (charge_function, rate_function)


def c(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [800, tdu_charge + numbers[0] - numbers[6]],
    ]
    rate_function = [
        [0, tdu_rate + numbers[3] / 100],
        [1201, tdu_rate + numbers[5] / 100],
    ]
    return (charge_function, rate_function)


def c1(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [800, tdu_charge + numbers[0] - numbers[8]],
    ]
    rate_function = [
        [0, tdu_rate + numbers[3] / 100],
        [1201, tdu_rate + numbers[5] / 100],
    ]
    return (charge_function, rate_function)


def c2(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [800, tdu_charge + numbers[0] - numbers[7]],
    ]
    rate_function = [
        [0, tdu_rate + numbers[4] / 100],
        [1201, tdu_rate + numbers[6] / 100],
    ]
    return (charge_function, rate_function)


def c3(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [800, tdu_charge + numbers[0] - numbers[9]],
    ]
    rate_function = [
        [0, tdu_rate + numbers[4] / 100],
        [1201, tdu_rate + numbers[6] / 100],
    ]
    return (charge_function, rate_function)


def c4(numbers, tdu_charge, tdu_rate):
    charge_function = [
        [0, tdu_charge + numbers[0]],
        [800, tdu_charge + numbers[0] - numbers[8]],
    ]
    rate_function = [
        [0, tdu_rate + numbers[4] / 100],
        [1201, tdu_rate + numbers[6] / 100],
    ]
    return (charge_function, rate_function)
