"""
ASHPense Accounts Module

Description:
This module powers the registration and management of user account
and profile
"""

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView

from apm_accounts.forms import ASHPenserCreationForm


# Create your views here. 
class ASHPenseSignoutView(LogoutView):
    """
    Logout from Platform 

    Description:
    The user is returned to the landing page upon clicking logout
    """

    next_page = reverse_lazy("login")

class ASHPenserSignupView(CreateView):
    """
    Registration Form
    
    Description:
    This class creates a form to register a new user for the platform
    """

    form_class = ASHPenserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"