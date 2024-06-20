"""
ASHPense Front-end Routes

Description:
This module specifies the paths to the various static files for
the front-end elements
"""

from django.urls import path
from apm_accounts.views import ASHPenserSignupView, ASHPenseSignoutView


urlpatterns = [
    path("signup/", ASHPenserSignupView.as_view(), name="signup"),
    path("logout/", ASHPenseSignoutView.as_view(), name="logout"), 
]
