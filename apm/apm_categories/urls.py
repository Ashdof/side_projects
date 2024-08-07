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

    ASHPenserCategoryUpdateView,
    ASHPenserSubCategoryUpdateView,
    ASHPenserPaymentMethodUpdateView,

    ASHPenserCategoryDeleteView,
    ASHPenserSubCategoryDeleteView,
    ASHPenserPaymentMethodDeleteView,

    ASHPenserCategoryCreateView,
    ASHPenserSubCategoryCreateView,
    ASHPenserPaymentMethodCreateView,
)

app_name="apm_categories"

urlpatterns = [
    # apm_categories
    path("apm_categories/", ASHPenserCategoryListView.as_view(), name="apm_categories_panel"), 
    path("apm_category_detail/<uuid:pk>", ASHPenserCategoryDetailView.as_view(), name="apm_category_detail"),
    path("<uuid:pk>/apm_category_delete", ASHPenserCategoryDeleteView.as_view(), name="apm_category_delete"),
    path("apm_category_update/<uuid:pk>", ASHPenserCategoryUpdateView.as_view(), name="apm_category_update"),
    path("apm_category_new/", ASHPenserCategoryCreateView.as_view(), name="apm_category_new"),

    # amp_subcategories
    path("apm_subcategory_detail/<uuid:pk>", ASHPenserSubCategoryDetailView.as_view(), name="apm_subcategory_detail"),
    path("<uuid:pk>/apm_subcategory_delete", ASHPenserSubCategoryDeleteView.as_view(), name="apm_subcategory_delete"),
    path("apm_subcategory_update/<uuid:pk>", ASHPenserSubCategoryUpdateView.as_view(), name="apm_subcategory_update"),
    path("apm_subcategory_new/", ASHPenserSubCategoryCreateView.as_view(), name="apm_subcategory_new"),
    
    # apm_paymethods
    path("apm_paymethod_detail/<uuid:pk>", ASHPenserPaymentMethodDetailView.as_view(), name="apm_paymethod_detail"),
    path("<uuid:pk>/apm_paymethod_delete", ASHPenserPaymentMethodDeleteView.as_view(), name="apm_paymethod_delete"),
    path("apm_paymethod_update/<uuid:pk>", ASHPenserPaymentMethodUpdateView.as_view(), name="apm_paymethod_update"),
    path("apm_paymethod_new/", ASHPenserPaymentMethodCreateView.as_view(), name="apm_paymethod_new")
]