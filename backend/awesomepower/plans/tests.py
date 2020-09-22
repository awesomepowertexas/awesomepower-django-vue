from decimal import Decimal

import pytest
from pandas.core.frame import DataFrame

from awesomepower.plans.business_logic import (
    calculate_plan_cost,
    filter_plans_by_zip_code,
    get_ptc_plan_df,
)
from awesomepower.plans.models import Plan, Provider, Tdu


@pytest.mark.django_db
def test_models():
    tdu = Tdu.objects.first()
    provider = Provider.objects.first()
    plan = Plan.objects.first()

    assert str(tdu) == tdu.name
    assert str(provider) == provider.name
    assert str(plan) == plan.name
    assert plan.provider_module.name == plan.provider.name

    plan.save_usage_costs(
        charge_function=[
            [Decimal("0"), Decimal("12.80")],
            [Decimal("500"), Decimal("7.85")],
            [Decimal("1000"), Decimal("-42.15")],
            [Decimal("1501"), Decimal("-17.15")],
        ],
        rate_function=[[Decimal("0"), Decimal("0.107312")]],
        successful_function_name="a",
    )

    assert plan.low_usage_rate == Decimal("0.1199")
    assert plan.medium_usage_rate == Decimal("0.0960")
    assert plan.high_usage_rate == Decimal("0.0949")

    plan.kwh_500 = round(
        calculate_plan_cost(plan.charge_function, plan.rate_function, 500) / 500, 3
    )
    plan.kwh_1000 = round(
        calculate_plan_cost(plan.charge_function, plan.rate_function, 1000) / 1000, 3
    )
    plan.kwh_2000 = round(
        calculate_plan_cost(plan.charge_function, plan.rate_function, 2000) / 2000, 3
    )
    plan.save()

    assert plan.matches_cost_functions(plan.charge_function, plan.rate_function)

    plan.reset_efl_numbers()

    assert plan.efl_numbers is None
    assert plan.charge_function is None
    assert plan.rate_function is None
    assert plan.successful_function_name is None
    assert plan.low_usage_rate is None
    assert plan.medium_usage_rate is None
    assert plan.high_usage_rate is None


@pytest.mark.django_db
def test_list_all_plans(client):
    response = client.get("/plans")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == len(Plan.objects.all())


@pytest.mark.django_db
def test_list_plans_valid_zip(client):
    zip_code = "75229"
    response = client.get(f"/plans?zip_code={zip_code}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == len(
        filter_plans_by_zip_code(Plan.objects.all(), zip_code)
    )


@pytest.mark.django_db
def test_list_plans_invalid_zip(client):
    zip_code = "00000"
    response = client.get(f"/plans?zip_code={zip_code}")

    assert response.status_code == 200
    assert type(response.json()) == list
    assert len(response.json()) == 0


def test_get_ptc_plan_df():
    plan_df = get_ptc_plan_df()
    assert type(plan_df) == DataFrame


def test_calculate_plan_cost():
    def plan_cost(plan, kwh_usage):
        return calculate_plan_cost(
            charge_function=plan["charge_function"],
            rate_function=plan["rate_function"],
            kwh_usage=kwh_usage,
        )

    plan_1 = {
        "charge_function": [
            [Decimal("0"), Decimal("12.80")],
            [Decimal("500"), Decimal("7.85")],
            [Decimal("1000"), Decimal("-42.15")],
            [Decimal("1501"), Decimal("-17.15")],
        ],
        "rate_function": [[Decimal("0"), Decimal("0.107312")]],
    }
    plan_2 = {
        "charge_function": [
            [Decimal("0"), Decimal("14.22")],
            [Decimal("800"), Decimal("-15.78")],
        ],
        "rate_function": [
            [Decimal("0"), Decimal("0.120929")],
            [Decimal("1201"), Decimal("0.169929")],
        ],
    }

    assert plan_cost(plan_1, 1) == Decimal("12.907312")
    assert plan_cost(plan_1, 499) == Decimal("66.348688")
    assert plan_cost(plan_1, 500) == Decimal("61.506000")
    assert plan_cost(plan_1, 501) == Decimal("61.613312")
    assert plan_cost(plan_1, 999) == Decimal("115.054688")
    assert plan_cost(plan_1, 1000) == Decimal("65.162000")
    assert plan_cost(plan_1, 1001) == Decimal("65.269312")
    assert plan_cost(plan_1, 1499) == Decimal("118.710688")
    assert plan_cost(plan_1, 1500) == Decimal("118.818000")
    assert plan_cost(plan_1, 1501) == Decimal("143.925312")
    assert plan_cost(plan_1, 1999) == Decimal("197.366688")
    assert plan_cost(plan_1, 2000) == Decimal("197.474000")
    assert plan_cost(plan_1, 2001) == Decimal("197.581312")

    assert plan_cost(plan_2, 1) == Decimal("14.340929")
    assert plan_cost(plan_2, 499) == Decimal("74.563571")
    assert plan_cost(plan_2, 500) == Decimal("74.684500")
    assert plan_cost(plan_2, 501) == Decimal("74.805429")
    assert plan_cost(plan_2, 999) == Decimal("105.028071")
    assert plan_cost(plan_2, 1000) == Decimal("105.149000")
    assert plan_cost(plan_2, 1001) == Decimal("105.269929")
    assert plan_cost(plan_2, 1499) == Decimal("180.094571")
    assert plan_cost(plan_2, 1500) == Decimal("180.264500")
    assert plan_cost(plan_2, 1501) == Decimal("180.434429")
    assert plan_cost(plan_2, 1999) == Decimal("265.059071")
    assert plan_cost(plan_2, 2000) == Decimal("265.229000")
    assert plan_cost(plan_2, 2001) == Decimal("265.398929")
