"""
ASHPense Earnings Front-end Routes

Description:
Specifies the paths to the various static files for the front-end elements
"""

from django.urls import path

from apm_earnings.views import (
    ASHPenserEarningsListView,
    ASHPenserEarningsDetailView,
    ASHPenserEarningUpdateView,
    ASHPenserEarningDeleteView,
    ASHPenserEarningCreateView
)


app_name="apm_earnings"

urlpatterns = [
    path("apm_earnings/", ASHPenserEarningsListView.as_view(), name="apm_earnings_panel"),
    path("apm_earnings_detail/<uuid:pk>", ASHPenserEarningsDetailView.as_view(), name="apm_earnings_detail"),
    path("apm_earnings_update/<uuid:pk>", ASHPenserEarningUpdateView.as_view(), name="apm_earnings_update"),
    path("<uuid:pk>/apm_earnings_delete", ASHPenserEarningDeleteView.as_view(), name="apm_earnings_delete"),
    path("apm_earnings_new/", ASHPenserEarningCreateView.as_view(), name="apm_earnings_new"),
]