"""
ASHPense Categories Front-end Routes

Description:
Specifies the paths to the various static files for the front-end elements
"""

from django.urls import path

from apm_categories.views import ASHPenserCategoryListView

app_name="apm_categories"

urlpatterns = [
    path("apm_categories/", ASHPenserCategoryListView.as_view(), name="apm_categories_panel"),
]