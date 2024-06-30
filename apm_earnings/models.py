"""
Database Module

Description:
Specify the database table and fields for tracking income
transactions
"""

from django.db import models
from django.conf import settings
from django.db import models
from django.shortcuts import reverse

import uuid

from apm_categories.models import ASHPenserCategories, ASHPenserPaymentMethod


class ASHPenserEarnings(models.Model):
    """
    Setup Income Transaction Model

    Description:
    Sets up database model for recording incomes
    """

    class Meta:
        verbose_name_plural = "EarningsData"
        db_table = "income_earnings"
        ordering = ("date", "category", "payer", "payment_method",)

    earn_data = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ashpenser_data = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField() 
    category = models.ForeignKey(ASHPenserCategories, on_delete=models.CASCADE)
    payer = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.ForeignKey(ASHPenserPaymentMethod, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return a string representation of this object"""

        return f"{self.amount}"
    
    def get_earn_date(self):
        """Return the amount and date for earning"""

        return f"{self.amount}-{self.date}"
    
    def get_absolute_url(self):
        return reverse("apm_earnings:apm_earnings_detail", kwargs={"pk": self.pk})