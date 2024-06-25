"""
ASHPense Categories View
"""

from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from apm_categories.models import (
    ASHPenserCategories,
    ASHPenserSubCategories,
    ASHPenserPaymentMethod
)


# Create your views here.
class ASHPenserCategoryListView(LoginRequiredMixin, TemplateView):
    """
    Categories List View

    Description:
    Creates a view for the display of categories list
    """

    # model = ASHPenserCategories
    template_name = "apm_categories/apm_categories_panel.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["apm_categories"] = ASHPenserCategories.objects.all()
        context["apm_subcategories"] = ASHPenserSubCategories.objects.all()
        context["apm_paymethods"] = ASHPenserPaymentMethod.objects.all()

        return context


class ASHPenserCategoryDetailView(LoginRequiredMixin, DetailView):
    """
    Display Category Object Details

    Description:
    Displays the details of a selected category object
    """

    model = ASHPenserCategories
    template_name = "apm_categories/apm_category_detail.html"


class ASHPenserSubCategoryDetailView(LoginRequiredMixin, DetailView):
    """
    Display Sub-category Object Details

    Description:
    Displays the details of a selected sub-category object
    """

    model = ASHPenserSubCategories
    template_name = "apm_categories/apm_subcategory_detail.html"


class ASHPenserPaymentMethodDetailView(LoginRequiredMixin, DetailView):
    """
    Display Payment method Object Details

    Description:
    Displays the details of a selected sub-category object
    """

    model = ASHPenserPaymentMethod
    template_name = "apm_categories/apm_paymethod_detail.html"