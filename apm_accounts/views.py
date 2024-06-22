"""
ASHPense Accounts Module

Description:
This module powers the registration and management of user account
and profile
"""

from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login, logout

from apm_accounts.forms import ASHPenserCreationForm, ASHPenserLoginForm


class ASHPenserSignupView(CreateView):
    """
    Registration Form View
    
    Description:
    Creates a form to register a new user for the platform
    """

    form_class = ASHPenserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ASHPenserLoginView(View):
    """
    Login View

    Description:
    Creates a login view for user login
    """

    form_class = ASHPenserLoginForm
    template_name = "login.html"

    def get(self, request):
        """
        Obtain Login Form

        Description:
        This method loads the custom login form

        Args:
        request (http request): the requested http resources

        Returns:
        The login form
        """

        form = self.form_class()

        return render(request, self.template_name, {"form": form})
    
    def post(self, request):
        """
        Login User

        Description:
        Analyzes user credentials with database values. If successful,
        redirects user to the right page

        Args:
        request (http request): the requested http resources

        Returns:
        Redirects to the dashboard if successful, otherwise print an error
        message
        """

        form = self.form_class(request.POST)
        err_msg = "Invalid email address or password. Please correct the error"

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request=request, email=email, password=password)

            if user is None:
                form.add_error(None, err_msg)
            else:
                login(request=request, user=user)
                return HttpResponseRedirect(reverse("home"))
        
        return render(request, self.template_name, {"form": form})


# Create your views here. 
class ASHPenseLogoutView(View):
    """
    Logout View

    Description:
    Redirects the user to the landing page upon clicking logout
    """

    def get(self, request):
        """
        Logout

        Description:
        Logs user out of the platform

        Args:
        request (http request): the requested http resource

        Returns:
        Redirects to the landing page
        """

        logout(request)

        return HttpResponseRedirect(reverse_lazy("index"))