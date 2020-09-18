import math

from django.core.management.base import BaseCommand

from awesomepower.plans.business_logic import get_ptc_plan_df
from awesomepower.plans.models import Provider, Tdu
from awesomepower.plans.providers import provider_modules
from awesomepower.plans.tdus import TDUS


class Command(BaseCommand):
    help = "Update the TDU and provider tables"

    def handle(self, *args, **options):
        update_tdu_table()
        update_provider_table()


def update_tdu_table():
    for tdu_dict in TDUS:
        tdu = Tdu.objects.filter(name=tdu_dict["name"])

        if tdu:
            tdu.update(**tdu_dict)
        else:
            Tdu.objects.create(**tdu_dict)


def update_provider_table():
    # add new providers from the modules to the database
    for module in provider_modules:
        if not Provider.objects.filter(name=module.name).exists():
            Provider.objects.create(name=module.name, ptc_name=module.ptc_name)

    # remove outdated providers from database
    provider_names = [module.name for module in provider_modules]

    for provider in Provider.objects.all():
        provider.is_active = bool(provider.name in provider_names)
        provider.save()

    # update provider ratings
    plan_df = get_ptc_plan_df()

    rating_df = plan_df.loc[:, ["[RepCompany]", "[Rating]"]]
    rating_dict = {rating[0]: rating[1] for rating in rating_df.values.tolist()}

    for provider_name, rating in rating_dict.items():
        provider = Provider.objects.filter(ptc_name=provider_name).first()
        if provider and not math.isnan(rating):
            provider.rating = rating
            provider.save()
