"""
Forms Module

Description:
Specify form fields for tracking income earnings
"""

from django import forms

from apm_earnings.models import ASHPenserEarnings


class DateInput(forms.DateInput):
    """Set up date input"""

    input_type = "date"


class ASHPenserEarningsForm(forms.ModelForm):
    """
    Earnings Form

    Description:
    Creates a form for adding and editing incomes earnings
    """

    class Meta:
        model = ASHPenserEarnings
        fields = ["date", "category", "payer", "payment_method", "amount", "description"]
        widgets = {
            "date": DateInput(),
        }