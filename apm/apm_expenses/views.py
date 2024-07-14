"""
ASHPense Expenses View Module
"""

from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    TemplateView, 
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)

from apm_expenses.models import ASHPenserExpenses
from apm_expenses.forms import ASHPenserExpensesForm


class ASHPenserExpensesView(LoginRequiredMixin, TemplateView):
    """
    Expenses List View

    Description:
    Creates a view for displaying list of expenses
    """

    template_name = "apm_expenses/apm_expenses_panel.html"

    def get_queryset(self):
        """Filter users"""

        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        """
        Get Context Data

        Descriptions:
        Loads data from expenses model by the currently logged
        in user
        """

        context = super().get_context_data(**kwargs)
        context["apm_expenses"] = ASHPenserExpenses.objects.filter(ashpenser_data=self.request.user)

        return context


class ASHPenserExpensesDetailView(LoginRequiredMixin, DetailView):
    """
    Display Expense Object Details

    Description:
    Displays the details of a selected expense object
    """

    model = ASHPenserExpenses
    template_name = "apm_expenses/details/apm_expenses_detail.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj


class ASHPenserExpensesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Update Expense Object Data

    Description
    Displays form to update data of an expense object
    """

    model = ASHPenserExpenses
    form_class = ASHPenserExpensesForm
    template_name = "apm_expenses/update/apm_expenses_update.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj
    
    def test_func(self):
        """
        RestrictAccess
        
        Description:
        Restricts updatinge an object to only those created by the currently
        logged-in user 
        """
        obj = self.get_object()

        return obj.ashpenser_data == self.request.user


class ASHPenserExpenseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete an Object

    Description:
    Deletes a selected object
    """

    model = ASHPenserExpenses
    template_name = "apm_expenses/delete/apm_expenses_delete.html"
    success_url = reverse_lazy("apm_expenses:apm_expenses_panel")

    def get_object(self, queryset=None):
        """Fetch resources by current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")

        return obj

    def delete(self, request, *args, **kwargs):
        """Delete the selected object"""

        info_msg = "Expense data deleted."
        messages.success(request, info_msg)

        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        """
        RestrictAccess
        
        Description:
        Restricts updatinge an object to only those created by the currently
        logged-in user
        """
        obj = self.get_object()

        return obj.ashpenser_data == self.request.user


class ASHPenserExpenseCreateView(LoginRequiredMixin, CreateView):
    """
    Create Expense Object

    Description:
    Creates a new expense object
    """

    model = ASHPenserExpenses
    form_class = ASHPenserExpensesForm
    template_name = "apm_expenses/new/apm_expenses_new.html"
    success_url = reverse_lazy("apm_expenses:apm_expenses_panel")

    def form_valid(self, form):
        """Commit resources to the database by user"""

        form.instance.ashpenser_data = self.request.user
        
        return super().form_valid(form)