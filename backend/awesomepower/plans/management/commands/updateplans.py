import inspect
import math
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from awesomepower.plans.business_logic import get_ptc_plan_df
from awesomepower.plans.models import Plan, Provider, Tdu


class Command(BaseCommand):
    help = "Update the plan table"

    def handle(self, *args, **options):
        add_ptc_plans_to_db()
        add_charges_rates()


def add_ptc_plans_to_db():
    plan_df = get_ptc_plan_df()

    # convert plans to Awesome Power data model
    column_map = {
        "[TduCompanyName]": "tdu_ptc_name",
        "[RepCompany]": "provider_ptc_name",
        "[Product]": "name",
        "[idKey]": "ptc_idkey",
        "[kwh500]": "kwh_500",
        "[kwh1000]": "kwh_1000",
        "[kwh2000]": "kwh_2000",
        "[Fixed]": "rate_type",
        "[PrePaid]": "is_prepaid",
        "[TimeOfUse]": "is_time_of_use",
        "[Promotion]": "is_promotion",
        "[NewCustomer]": "is_new_customer",
        "[Renewable]": "percent_renewable",
        "[TermValue]": "term",
        "[CancelFee]": "cancellation_fee",
        "[Language]": "language",
        "[TermsURL]": "terms_url",
        "[FactsURL]": "facts_url",
        "[EnrollURL]": "enroll_url",
        "[EnrollPhone]": "enroll_phone",
    }
    plan_df = plan_df.rename(columns=column_map)
    plan_df = plan_df.filter(list(column_map.values()))
    plan_df = plan_df.replace(
        {
            "language": {
                "English": Plan.LANGUAGE_ENGLISH,
                "Spanish": Plan.LANGUAGE_SPANISH,
            }
        }
    )
    for url in ["terms_url", "facts_url", "enroll_url"]:
        plan_df[url] = plan_df.apply(lambda x: str(x[url]).replace(" ", "%20"), axis=1)
    for kwh in ["kwh_500", "kwh_1000", "kwh_2000"]:
        plan_df[kwh] = plan_df[kwh].astype(str)

    ptc_plans = plan_df.to_dict(orient="records")

    # set is_active for every plan
    for plan in Plan.objects.all():
        plan.is_active = bool(str(plan.ptc_idkey) in plan_df["ptc_idkey"].values)
        try:
            plan.save()
        except ValidationError:
            plan.delete()

    for plan_dict in ptc_plans:
        tdu = Tdu.objects.filter(ptc_name=plan_dict.pop("tdu_ptc_name")).first()
        provider = Provider.objects.filter(
            ptc_name=plan_dict.pop("provider_ptc_name"), is_active=True
        ).first()
        if not tdu or not provider:
            continue

        if math.isnan(plan_dict["percent_renewable"]):
            continue

        # process URL for certain providers
        if any(
            substr in plan_dict["facts_url"]
            for substr in ["4changeenergy.com", "myexpressenergy.com"]
        ):
            plan_dict["facts_url"] = (
                plan_dict["facts_url"]
                .replace("viewpdf.aspx/?Docs", "efls")
                .replace("viewpdf.aspx/?", "")
                .replace("Docs", "efls")
            )

        # create or update database plan
        plan = Plan.objects.filter(ptc_idkey=plan_dict["ptc_idkey"])
        try:
            if plan:
                # reset efl_numbers when kWhs differ
                if (
                    Decimal(plan_dict["kwh_500"]) != plan[0].kwh_500
                    or Decimal(plan_dict["kwh_1000"]) != plan[0].kwh_1000
                    or Decimal(plan_dict["kwh_2000"]) != plan[0].kwh_2000
                ):
                    plan[0].reset_efl_numbers()

                plan.update(tdu=tdu, provider=provider, **plan_dict)
            else:
                Plan.objects.create(tdu=tdu, provider=provider, **plan_dict)
        except Exception as e:
            print(plan_dict["ptc_idkey"])
            print(e)


def add_charges_rates():
    for plan in Plan.objects.active_english().order_by(
        "provider__name", "name", "tdu__name"
    ):
        # skip plans that already have valid cost functions
        if (
            plan.charge_function
            and plan.rate_function
            and plan.matches_cost_functions(plan.charge_function, plan.rate_function)
        ):
            # recalculate usage costs in case we change the calculation method
            plan.save_usage_costs(
                plan.charge_function, plan.rate_function, plan.successful_function_name
            )
            continue

        if plan.efl_numbers is None:
            plan.set_efl_numbers()

            if plan.efl_numbers is None:
                plan.efl_numbers = []
                plan.save()
                continue

        for tdu_charge in plan.tdu.charges:
            for tdu_rate in plan.tdu.rates:
                # try all functions in the provider_module to see if they return the
                # correct cost functions
                for function in inspect.getmembers(
                    plan.provider_module, inspect.isfunction
                ):
                    try:
                        charge_function, rate_function = function[1](
                            numbers=plan.efl_numbers,
                            tdu_charge=tdu_charge,
                            tdu_rate=tdu_rate,
                        )
                    except IndexError:
                        continue

                    # convert cutoffs to Decimal so we can store them in the ArrayField
                    for piece in charge_function:
                        piece[0] = round(Decimal(str(piece[0])), 2)
                        piece[1] = round(Decimal(str(piece[1])), 2)
                    for piece in rate_function:
                        piece[0] = round(Decimal(str(piece[0])), 6)
                        piece[1] = round(Decimal(str(piece[1])), 6)

                    if plan.matches_cost_functions(charge_function, rate_function):
                        plan.save_usage_costs(
                            charge_function, rate_function, function[0]
                        )
