"""
ASHPense Expenses Front-end Routes

Description:
Specifies the paths to the various static files for the front-end elements
"""

from django.urls import path

from apm_expenses.views import (
    ASHPenserExpensesView,
    ASHPenserExpensesDetailView,
    ASHPenserExpensesUpdateView,
    ASHPenserExpenseDeleteView,
    ASHPenserExpenseCreateView,
)


app_name="apm_expenses"

urlpatterns = [
    path("apm_expenses/", ASHPenserExpensesView.as_view(), name="apm_expenses_panel"),
    path("apm_expenses_detail/<uuid:pk>", ASHPenserExpensesDetailView.as_view(), name="apm_expenses_detail"),
    path("apm_expenses_update/<uuid:pk>", ASHPenserExpensesUpdateView.as_view(), name="apm_expenses_update"),
    path("<uuid:pk>/apm_expenses_delete", ASHPenserExpenseDeleteView.as_view(), name="apm_expenses_delete"),
    path("apm_expenses_new/", ASHPenserExpenseCreateView.as_view(), name="apm_expenses_new"),
]