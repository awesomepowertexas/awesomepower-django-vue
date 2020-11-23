import io
import re
from decimal import Decimal
from functools import reduce

import numpy as np
import requests
import urllib3
from django.contrib.postgres.fields import ArrayField
from django.db import models
from google.api_core import retry
from google.api_core.exceptions import GoogleAPIError
from google.cloud import vision
from html2text import html2text
from pdf2image import convert_from_bytes
from pdf2image.exceptions import PDFPageCountError, PDFSyntaxError
from scipy.stats import skewnorm

from awesomepower.plans.providers import provider_modules

from ..models import BaseModel
from .business_logic import calculate_plan_cost

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Tdu(BaseModel):
    name = models.TextField()
    ptc_name = models.TextField()
    charges = ArrayField(models.DecimalField(max_digits=4, decimal_places=2))
    rates = ArrayField(models.DecimalField(max_digits=6, decimal_places=6))

    def __str__(self):
        return self.name


class Provider(BaseModel):
    name = models.TextField()
    ptc_name = models.TextField()
    is_active = models.BooleanField(default=True)
    rating = models.IntegerField(default=-1)

    def __str__(self):
        return self.name


class PlanManager(models.Manager):
    def active_english(self):
        return self.get_queryset().filter(
            is_active=True, language=Plan.LANGUAGE_ENGLISH
        )


class Plan(BaseModel):
    RATE_VARIABLE = 0
    RATE_FIXED = 1
    RATE_INDEXED = 2
    RATE_CHOICES = [
        (RATE_VARIABLE, "Variable"),
        (RATE_FIXED, "Fixed"),
        (RATE_INDEXED, "Indexed"),
    ]

    LANGUAGE_ENGLISH = 0
    LANGUAGE_SPANISH = 1
    LANGUAGE_CHOICES = [(LANGUAGE_ENGLISH, "English"), (LANGUAGE_SPANISH, "Spanish")]

    tdu = models.ForeignKey(Tdu, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    name = models.TextField()
    is_active = models.BooleanField(default=True)

    efl_numbers = ArrayField(
        models.DecimalField(max_digits=10, decimal_places=6), null=True, blank=True
    )
    charge_function = ArrayField(
        ArrayField(models.DecimalField(max_digits=6, decimal_places=2), size=2),
        null=True,
        blank=True,
    )
    rate_function = ArrayField(
        ArrayField(models.DecimalField(max_digits=10, decimal_places=6), size=2),
        null=True,
        blank=True,
    )
    successful_function_name = models.CharField(max_length=3, null=True, blank=True)
    low_usage_rate = models.DecimalField(
        max_digits=4, decimal_places=4, null=True, blank=True
    )
    medium_usage_rate = models.DecimalField(
        max_digits=4, decimal_places=4, null=True, blank=True
    )
    high_usage_rate = models.DecimalField(
        max_digits=4, decimal_places=4, null=True, blank=True
    )

    ptc_idkey = models.IntegerField()
    kwh_500 = models.DecimalField(max_digits=3, decimal_places=3)
    kwh_1000 = models.DecimalField(max_digits=3, decimal_places=3)
    kwh_2000 = models.DecimalField(max_digits=3, decimal_places=3)
    rate_type = models.IntegerField(choices=RATE_CHOICES)
    is_prepaid = models.BooleanField()
    is_time_of_use = models.BooleanField()
    is_promotion = models.BooleanField()
    is_new_customer = models.BooleanField()
    percent_renewable = models.IntegerField()
    term = models.IntegerField()
    cancellation_fee = models.TextField()
    language = models.IntegerField(choices=LANGUAGE_CHOICES)

    terms_url = models.URLField(max_length=500)
    facts_url = models.URLField(max_length=500)
    enroll_url = models.URLField(max_length=500)
    enroll_phone = models.TextField()

    objects = PlanManager()

    @property
    def provider_module(self):
        return next(
            module for module in provider_modules if module.name == self.provider.name
        )

    def __str__(self):
        return self.name

    def set_efl_numbers(self):  # pragma: no cover
        # make request to EFL PDF URL
        try:
            response = requests.get(
                self.facts_url,
                headers={"User-Agent": "Mozilla/5.0"},
                stream=True,
                timeout=10,
                verify=False,
            )
        except requests.exceptions.RequestException:
            return

        if "content-type" not in response.headers:
            return

        content_type = response.headers["content-type"].lower()

        # convert HTML response to raw text
        if content_type.startswith("text/html"):
            efl_text = html2text(response.text)

        # convert PDF response to JPEG
        elif content_type.startswith("application/pdf") or content_type.startswith(
            "application/octet-stream"
        ):
            try:
                image_file = convert_from_bytes(
                    response.content, fmt="JPEG", first_page=1, last_page=1
                )[0]
            except (
                requests.exceptions.RequestException,
                PDFPageCountError,
                PDFSyntaxError,
            ):
                return

            image_bytesio = io.BytesIO()
            image_file.save(image_bytesio, format="JPEG")

            # run document text detection in GCP
            vision_client = vision.ImageAnnotatorClient()
            vision_image = vision.Image(content=image_bytesio.getvalue())
            try:
                response = vision_client.document_text_detection(
                    image=vision_image, retry=retry.Retry()
                )
                efl_text = response.full_text_annotation.text
            except GoogleAPIError:
                return

        # unhandled content-type
        else:
            return

        if efl_text is None:
            return

        for start_text in self.provider_module.start_texts:
            efl_numbers = [
                round(Decimal(x), 6)
                for x in re.findall(
                    r"[\d]+[\.]?\d*", efl_text[efl_text.find(start_text) :]
                )
                if Decimal(x) < Decimal("10000")
            ]

            if efl_numbers:
                self.efl_numbers = efl_numbers
                self.save()

    def matches_cost_functions(self, charge_function, rate_function):
        cost_500 = calculate_plan_cost(charge_function, rate_function, 500) / 500
        cost_1000 = calculate_plan_cost(charge_function, rate_function, 1000) / 1000
        cost_2000 = calculate_plan_cost(charge_function, rate_function, 2000) / 2000
        prec = 0.0015

        return bool(
            abs(cost_500 - self.kwh_500) <= prec
            and abs(cost_1000 - self.kwh_1000) <= prec
            and abs(cost_2000 - self.kwh_2000) <= prec
        )

    def save_usage_costs(
        self, charge_function, rate_function, successful_function_name
    ):
        def weighted_cost(distribution):
            return reduce(
                lambda total, toople: total
                + calculate_plan_cost(charge_function, rate_function, toople[0] * 5 + 5)
                * Decimal(str(toople[1] * 5)),
                enumerate(distribution),
                0,
            )

        linspace = np.linspace(5, 5000, num=1000)
        usage_dist = {
            "low": {"a": 5, "loc": 250, "scale": 400},
            "medium": {"a": 4, "loc": 500, "scale": 700},
            "high": {"a": 3, "loc": 1000, "scale": 1000},
        }

        usage_cost = {}
        usage_mean = {}

        for dist_name in ["low", "medium", "high"]:
            usage_cost[dist_name] = weighted_cost(
                skewnorm.pdf(
                    linspace,
                    usage_dist[dist_name]["a"],
                    usage_dist[dist_name]["loc"],
                    usage_dist[dist_name]["scale"],
                )
            )
            usage_mean[dist_name] = Decimal(
                str(
                    skewnorm.mean(
                        usage_dist[dist_name]["a"],
                        usage_dist[dist_name]["loc"],
                        usage_dist[dist_name]["scale"],
                    )
                )
            )

        self.charge_function = charge_function
        self.rate_function = rate_function
        self.successful_function_name = successful_function_name

        self.low_usage_rate = round(usage_cost["low"] / usage_mean["low"], 4)
        self.medium_usage_rate = round(usage_cost["medium"] / usage_mean["medium"], 4)
        self.high_usage_rate = round(usage_cost["high"] / usage_mean["high"], 4)

        self.save()

    def reset_efl_numbers(self):
        self.efl_numbers = None
        self.charge_function = None
        self.rate_function = None
        self.successful_function_name = None
        self.low_usage_rate = None
        self.medium_usage_rate = None
        self.high_usage_rate = None

        self.save()
