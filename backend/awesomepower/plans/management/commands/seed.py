import random

from django.core.management import call_command
from django.core.management.base import BaseCommand

from awesomepower.plans.factories import PlanFactory
from awesomepower.plans.models import Plan, Provider, Tdu


class Command(BaseCommand):
    help = "Seeds the database"

    def handle(self, *args, **options):
        print("Seeding database...")

        call_command("flush", "--no-input")

        call_command("updatetdusproviders", "--skip-ratings")

        for tdu in Tdu.objects.all():
            for provider in Provider.objects.all():
                PlanFactory(tdu=tdu, provider=provider)

            for plan in Plan.objects.filter(tdu=tdu)[:2]:
                plan.term = 12
                plan.save()

        for provider in Provider.objects.all():
            provider.rating = random.randint(1, 5)
            provider.save()

        print("Database seeded successfully")
