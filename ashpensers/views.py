"""
Profile Vies Module
"""

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView
)

from ashpensers.models import ASHPensersProfile
from ashpensers.forms import (
    ASHPenserForm,
    ASHPensersProfileChangeForm,
    ASHPenserPasswordChangeForm,
    # ASHPensersProfilePasswordChangeForm
)

from apm_accounts.models import ASHPenser
# from apm_accounts.forms import ASHPenserChangeForm


class ASHPensersProfilePanelView(LoginRequiredMixin, TemplateView):
    """
    Profile Page Panel

    Description:
    Displays the profile page of the currently logged-in user
    """

    template_name = "apm_mensers/apm_mensers_panel.html"


class ASHPensersProfileDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete User Object

    Description:
    Enables a user to delete his profile
    """

    model = ASHPensersProfile
    template_name = "apm_mensers/delete/apm_mensers_delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        """Fetch data of the currently logged-in user"""
        
        return self.request.user


class ASHPensersPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """
    Change User Password

    Descroption:
    Enables the currently logged-in user to change password
    """

    # form_class = ASHPenserPasswordChangeForm
    # template_name = "apm_mensers/registration/apm_mensers_password_change.html"
    # success_url = reverse_lazy("apm_mensers:apm_mensers_panel")

    def get(self, request, *args, **kwargs):
        """Fetch resources of the currently logged-in user"""

        form = ASHPenserPasswordChangeForm(self.request.user)

        return render(
            request,
            "apm_mensers/registration/apm_mensers_password_change.html",
            {"apm_mensers_password_form": form}
        )
    
    def post(self, request, *args, **kwargs):
        """
        Save Form

        Description:
        Commits form with only valid values to the database
        """

        form = ASHPenserPasswordChangeForm(self.request.user, self.request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed.")

            return redirect("apm_mensers:apm_mensers_panel")
        else:
            messages.error(request, "Some fields have invalid values, please correct them.")

        return render(
            request,
            "apm_mensers/registration/apm_mensers_password_change.html",
            {"apm_mensers_password_form": form}
        )
    
    def test_func(self):
        """
        Check User

        Description:
        Checks if user is authenticated and is the owner of the account
        """
        
        return self.request.user.is_authenticated and self.request.user.pk == self.get_object().user.pk
    
    # def get_context_data(self, **kwargs):
    #     """Setup context data for the user object"""

    #     context = super().get_context_data(**kwargs)
    #     context["ashpenser_form"] = ASHPenserForm(instance=self.request.user)

    #     return context


class ASHPensersProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update Profile

    Description: 
    Enables the currently logged-in user to edit profile information
    """

    model = ASHPensersProfile
    form_class = ASHPensersProfileChangeForm
    template_name = "apm_mensers/updates/apm_mensers_update.html"
    success_url = reverse_lazy("apm_mensers:apm_mensers_panel")

    def get_object(self):
        """Fetch user profile object"""

        return self.request.user

    def get_context_data(self, **kwargs):
        """Setup context data for the user object"""

        context = super().get_context_data(**kwargs)
        context["ashpenser_form"] = ASHPenserForm(instance=self.request.user)
        context['apm_mensers_form'] = ASHPensersProfileChangeForm(instance=self.request.user.ashpensersprofile)

        return context

    def form_valid(self, form):
        """
        Save Form

        Description:
        Commits form with only valid values to the database
        """

        ashpenser_form = ASHPenserForm(self.request.POST, instance=self.request.user)
        apm_mensers_form = ASHPensersProfileChangeForm(self.request.POST, self.request.FILES, instance=self.request.user.ashpensersprofile)


        if apm_mensers_form.is_valid() and ashpenser_form.is_valid():
            ashpenser_form.save()
            apm_mensers_form.save()
            
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, ashpenser_form=ashpenser_form, apm_mensers_form=apm_mensers_form))