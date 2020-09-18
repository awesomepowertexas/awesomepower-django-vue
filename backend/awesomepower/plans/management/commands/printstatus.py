import inspect
import os
from collections import Counter

from django.core.management.base import BaseCommand

from awesomepower.plans.business_logic import get_ptc_plan_df
from awesomepower.plans.models import Plan, Provider
from awesomepower.plans.providers import provider_modules


class Command(BaseCommand):
    help = (
        "Print things that need to be updated about the codebase, due to new plans "
        "and providers"
    )

    def handle(self, *args, **options):
        os.system("./restore_db_from_prod.sh")

        plan_df = get_ptc_plan_df()
        print_uncaptured_providers(plan_df)
        print_unused_plan_functions()


def print_uncaptured_providers(plan_df):
    provider_df = plan_df.loc[:, ["[RepCompany]"]]
    provider_list = sorted([provider[0] for provider in provider_df.values.tolist()])
    provider_counter = Counter(provider_list).most_common()

    print("\n\n")
    print("UNCAPTURED PROVIDERS")
    print("====================")
    for (provider_ptc_name, num_plans) in provider_counter:
        if not Provider.objects.filter(ptc_name=provider_ptc_name).exists():
            print(f"{num_plans} plans: {provider_ptc_name}")


def print_unused_plan_functions():
    print("\n\n")
    print("UNUSED PLAN FUNCTIONS")
    print("=====================")
    for provider_module in provider_modules:
        provider = Provider.objects.get(name=provider_module.name)
        if not provider.is_active:
            continue

        for function in inspect.getmembers(provider_module, inspect.isfunction):
            plans = Plan.objects.active_english().filter(
                provider=provider, successful_function_name=function[0]
            )

            if not plans:
                print(provider_module.name, function[0])
