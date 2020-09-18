from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .business_logic import filter_plans_by_zip_code
from .models import Plan
from .serializers import PlanSerializer


class PlanList(ListAPIView):
    serializer_class = PlanSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Plan.objects.active_english().filter(
            low_usage_rate__isnull=False,
            medium_usage_rate__isnull=False,
            high_usage_rate__isnull=False,
        )

        zip_code = self.request.query_params.get("zip_code", None)

        if zip_code:
            queryset = filter_plans_by_zip_code(queryset, zip_code)

        return queryset
