from rest_framework.serializers import ModelSerializer

from .models import Plan, Provider, Tdu


class TduSerializer(ModelSerializer):
    class Meta:
        model = Tdu
        fields = ("name",)


class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ("name", "is_active", "rating")


class PlanSerializer(ModelSerializer):
    tdu = TduSerializer()
    provider = ProviderSerializer()

    class Meta:
        model = Plan
        fields = (
            "tdu",
            "provider",
            "name",
            "is_active",
            "charge_function",
            "rate_function",
            "low_usage_rate",
            "medium_usage_rate",
            "high_usage_rate",
            "ptc_idkey",
            "kwh_500",
            "kwh_1000",
            "kwh_2000",
            "rate_type",
            "is_prepaid",
            "is_time_of_use",
            "is_promotion",
            "is_new_customer",
            "percent_renewable",
            "term",
            "cancellation_fee",
            "language",
            "terms_url",
            "facts_url",
            "enroll_url",
            "enroll_phone",
        )
