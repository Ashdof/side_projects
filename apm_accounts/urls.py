"""
ASHPense Front-end Routes

Description:
This module specifies the paths to the various static files for
the front-end elements
"""

from django.urls import path
from apm_accounts.views import (
    ASHPenserSignupView,
    ASHPenseLogoutView,
    ASHPenserLoginView
)


urlpatterns = [
    path("signup/", ASHPenserSignupView.as_view(), name="signup"),
    path("apm_accounts/login/", ASHPenserLoginView.as_view(), name="login"),
    path("apm_accounts/logout/", ASHPenseLogoutView.as_view(), name="logout"), 
]
