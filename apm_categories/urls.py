"""
ASHPense Categories Front-end Routes

Description:
Specifies the paths to the various static files for the front-end elements
"""

from django.urls import path

from apm_categories.views import (
    ASHPenserCategoryListView,
    ASHPenserCategoryDetailView,
    ASHPenserSubCategoryDetailView,
    ASHPenserPaymentMethodDetailView,
)

app_name="apm_categories"

urlpatterns = [
    path("apm_categories/", ASHPenserCategoryListView.as_view(), name="apm_categories_panel"),
    path("apm_category_detail/<uuid:pk>", ASHPenserCategoryDetailView.as_view(), name="apm_category_detail"),
    path("apm_subcategory_detail/<uuid:pk>", ASHPenserSubCategoryDetailView.as_view(), name="apm_subcategory_detail"),
    path("apm_paymethod_detail/<uuid:pk>", ASHPenserPaymentMethodDetailView.as_view(), name="apm_paymethod_detail"),
]