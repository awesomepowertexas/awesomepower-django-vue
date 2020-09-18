from django.urls import path

from .plans.views import PlanList

urlpatterns = [path("plans", PlanList.as_view())]
