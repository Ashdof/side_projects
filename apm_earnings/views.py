"""
ASHPense Earnings View
"""

from django.http import Http404
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView, 
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)

from apm_earnings.models import ASHPenserEarnings
from apm_earnings.forms import ASHPenserEarningsForm


class ASHPenserEarningsListView(LoginRequiredMixin, TemplateView):
    """
    Earnings List View

    Description:
    Creates a view for displaying list of earnings
    """

    template_name = "apm_earnings/apm_earnings_panel.html"

    def get_queryset(self):
        """Filter users"""

        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        """
        Get Context Data

        Descriptions:
        Loads data from earnings model by the currently logged
        in user
        """

        context = super().get_context_data(**kwargs)
        context["apm_earnings"] = ASHPenserEarnings.objects.filter(ashpenser_data=self.request.user)

        return context


class ASHPenserEarningsDetailView(LoginRequiredMixin, DetailView):
    """
    Display Earning Object Details

    Description:
    Displays the details of a selected earning object
    """

    model = ASHPenserEarnings
    template_name = "apm_earnings/details/apm_earning_detail.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj


class ASHPenserEarningUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update Earning Object Data

    Description
    Displays form to update data of an earning's object
    """

    model = ASHPenserEarnings
    form_class = ASHPenserEarningsForm
    template_name = "apm_earnings/updates/apm_earnings_update.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj


class ASHPenserEarningDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete an Object

    Description:
    Deletes a selected object
    """

    model = ASHPenserEarnings
    template_name = "apm_earnings/delete/apm_earnings_delete.html"
    success_url = reverse_lazy("apm_earnings:apm_earnings_panel")

    def get_object(self, queryset=None):
        """Fetch resources by current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj

    def delete(self, request, *args, **kwargs):
        """Delete the selected object"""

        info_msg = "Category data deleted."
        messages.success(request, info_msg)
        return super().delete(request, *args, **kwargs)


class ASHPenserEarningCreateView(LoginRequiredMixin, CreateView):
    """
    Create Earning Object

    Description:
    Creates a new earning object
    """

    model = ASHPenserEarnings
    form_class = ASHPenserEarningsForm
    template_name = "apm_earnings/new/apm_earnings_new.html"
    success_url = reverse_lazy("apm_earnings:apm_earnings_panel")

    def form_valid(self, form):
        """Commit resources to the database by user"""

        form.instance.ashpenser_data = self.request.user
        return super().form_valid(form)