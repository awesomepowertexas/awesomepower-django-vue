import factory
import factory.django
import factory.fuzzy

from .models import Plan


class PlanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Plan

    name = factory.Faker("bs")
    low_usage_rate = factory.fuzzy.FuzzyDecimal(0.07, 0.15, 4)
    medium_usage_rate = factory.fuzzy.FuzzyDecimal(0.07, 0.15, 4)
    high_usage_rate = factory.fuzzy.FuzzyDecimal(0.07, 0.15, 4)
    ptc_idkey = factory.Sequence(lambda n: n)
    kwh_500 = factory.fuzzy.FuzzyDecimal(0.07, 0.15, 3)
    kwh_1000 = factory.fuzzy.FuzzyDecimal(0.07, 0.15, 3)
    kwh_2000 = factory.fuzzy.FuzzyDecimal(0.07, 0.15, 3)
    rate_type = 1
    is_prepaid = False
    is_time_of_use = False
    is_promotion = False
    is_new_customer = False
    percent_renewable = factory.fuzzy.FuzzyInteger(0, 100)
    term = factory.fuzzy.FuzzyInteger(1, 36)
    cancellation_fee = factory.fuzzy.FuzzyInteger(0, 500)
    language = 0
    terms_url = factory.Faker("url")
    facts_url = factory.Faker("url")
    enroll_url = factory.Faker("url")
    enroll_phone = factory.Faker("phone_number")
