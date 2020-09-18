import io

import pandas as pd
import requests


def get_ptc_plan_df():
    response = requests.get("http://powertochoose.org/en-us/Plan/ExportToCsv")
    plan_df = pd.read_csv(io.StringIO(response.text), error_bad_lines=False)
    plan_df = plan_df[:-1]  # remove "END OF FILE"
    plan_df = plan_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return plan_df


def filter_plans_by_zip_code(queryset, zip_code):
    response = requests.post(
        "http://powertochoose.com/en-us/service/v1/",
        json={
            "method": "TduCompaniesByZip",
            "zip_code": zip_code,
            "language": 0,
            "include_details": False,
        },
    )
    if not response or not response.json():
        return queryset.filter(name=None)

    tdu_ptc_name = response.json()[0]["company_name"]
    queryset = queryset.filter(tdu__ptc_name=tdu_ptc_name)

    return queryset


def calculate_plan_cost(charge_function, rate_function, kwh_usage):
    # find the charge piecewise function that the kWH usage falls into
    charge_index = len(charge_function) - 1
    for index, array in enumerate(charge_function):
        if kwh_usage < array[0]:
            charge_index = index - 1
            break

    charge = charge_function[charge_index][1]

    # find the rate piecewise function that the kWH usage falls into
    rate_index = len(rate_function) - 1
    for index, array in enumerate(rate_function):
        if kwh_usage <= array[0]:
            rate_index = index - 1
            break

    rate_total = 0

    # add the total of all rate piecewise functions before the last index
    for index in range(rate_index):
        rate_total += rate_function[index][1] * (
            rate_function[index + 1][0] - rate_function[index][0]
        )

    # add the remaining kWH of the final piecewise function
    rate_total += rate_function[rate_index][1] * (
        kwh_usage - rate_function[rate_index][0]
    )

    plan_cost = charge + rate_total

    return plan_cost
