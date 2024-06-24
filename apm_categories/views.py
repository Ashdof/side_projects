"""
ASHPense Categories View
"""

from django.shortcuts import render
from django.views.generic import ListView

from apm_categories.models import ASHPenserCategories


# Create your views here.
class ASHPenserCategoryListView(ListView):
    """
    Categories List View

    Description:
    Creates a view for the display of categories list
    """

    model = ASHPenserCategories
    template_name = "apm_categories/apm_categories_panel.html"
    context_object_name = "apm_categories"