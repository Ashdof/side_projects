"""
Database Module

Description:
Specify the database table and fields for tracking expense
transactions
"""

from django.db import models

from django.conf import settings
from django.shortcuts import reverse

import uuid

from apm_categories.models import (
    ASHPenserCategories,
    ASHPenserSubCategories,
    ASHPenserPaymentMethod,
)


class ASHPenserExpenses(models.Model):
    """
    Setup Expenses Transaction Model

    Description:
    Sets up database model for recording expenses
    """

    class Meta:
        verbose_name_plural = "ExpensesData"
        db_table = "expense_earning"
        ordering = ("date", "category", "subcategory", "payee", "payment_method",)

    expense_data = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ashpenser_data = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField() 
    category = models.ForeignKey(ASHPenserCategories, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(ASHPenserSubCategories, on_delete=models.CASCADE)
    payee = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.ForeignKey(ASHPenserPaymentMethod, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return a string representation of this object"""

        return f"{self.amount}"
    
    def get_expense_date(self):
        """Return the amount and date for expenditure"""

        return f"{self.amount}-{self.date}"
    
    def get_absolute_url(self):
        return reverse("apm_expenses:apm_expenses_detail", kwargs={"pk": self.pk})