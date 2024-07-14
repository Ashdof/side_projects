"""
Forms Module

Description:
Specify form fields for tracking expenses
"""

from django import forms

from apm_expenses.models import ASHPenserExpenses


class DateInput(forms.DateInput):
    """Set up date input"""

    input_type = "date"


class ASHPenserExpensesForm(forms.ModelForm):
    """
    Expenses Form

    Description:
    Creates a form for adding and editing expenses
    """

    class Meta:
        model = ASHPenserExpenses
        fields = ["date", "category", "subcategory", "payee", "payment_method", "amount", "description"]
        widgets = {
            "date": DateInput(),
        }