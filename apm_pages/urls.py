"""
Pages Routes

Description:
This specifies the paths for page switching
"""
from django.urls import path


from apm_pages.views import ASHPenserHomePageView


urlpatterns = [
    path("", ASHPenserHomePageView.as_view(), name="home"),
]
