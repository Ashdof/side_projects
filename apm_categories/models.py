"""
Database Model Specification

Description:
Specify the database tables for categories, subcategories and
payment methods
"""

from django.db import models
from django.conf import settings
from django.shortcuts import reverse

import uuid
import django_filters

from apm_accounts.choices import CATEGORY_TYPE


class ASHPenserCategories(models.Model):
    """
    Categories Model

    Description:
    Sets up database table for recording categories
    """

    class Meta:
        verbose_name_plural = "CategoriesData"
        db_table = "categories"
        ordering = ("date_created", "category_name",)

    category_data = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ashpenser_data = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories")
    date_created = models.DateTimeField(max_length=8)
    category_name = models.CharField(max_length=100, null=True, blank=True)
    category_type = models.CharField(max_length=100, choices=CATEGORY_TYPE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return a string representation of this object"""

        return f"{self.category_name}"
    
    def get_absolute_url(self):
        return reverse("apm_categories:categories_detail", kwargs={"pk": self.pk})


class ASHPenserCategoriesFilter(django_filters.FilterSet):
    """
    Create Filter
    
    Description:
    Provides filter capability for Categories Data
    """

    class Meta:
        model = ASHPenserCategories
        fields = ["date_created", "category_name",]