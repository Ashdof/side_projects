"""
Database Model Specification

Description:
Specify the database tables for categories, subcategories and
payment methods
"""

from django.db import models
from django.conf import settings
from django.urls import reverse

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
        ordering = ("category_name",)

    category_data = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ashpenser_data = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories")
    category_name = models.CharField(max_length=100, null=True, blank=True)
    category_type = models.CharField(max_length=100, choices=CATEGORY_TYPE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return a string representation of this object"""

        return f"{self.category_name}"
    
    def get_absolute_url(self):
        return reverse("apm_categories:apm_category_detail", kwargs={"pk": self.pk})


class ASHPenserCategoriesFilter(django_filters.FilterSet):
    """
    Create Filter
    
    Description:
    Provides filter capability for Categories Data
    """

    class Meta:
        model = ASHPenserCategories
        fields = ["category_name",]



class ASHPenserSubCategories(models.Model):
    """
    Sub-categories Model

    Description:
    Sets up database table for recording sub-categories
    """

    class Meta:
        verbose_name_plural = "SubCategoriesData"
        db_table = "subcategories"
        ordering = ("subcategory_name",) 

    subcategory_data = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ashpenser_data = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subcategories")
    category_data = models.ForeignKey(ASHPenserCategories, on_delete=models.CASCADE, related_name="subcategories")
    subcategory_name = models.CharField(max_length=100, null=True, blank=True)
    subcategory_type = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return a string representation of this object"""

        return f"{self.subcategory_name}"
    
    def get_absolute_url(self):
        return reverse("apm_categories:apm_subcategory_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        """
        Override Save Method

        Descriptions:
        Overrides the save method by including the of category types from
        the Categories table. These types uploaded to the categories
        field
        """

        if self.category_data is not None:
            self.subcategory_type = self.category_data.category_type
        
        super().save(*args, **kwargs)


class ASHPenserSubCategoriesFilter(django_filters.FilterSet):
    """
    Create Filter
    
    Description:
    Provides filter capability for Sub-categories Data
    """

    class Meta:
        model = ASHPenserSubCategories
        fields = ["subcategory_name",]


class ASHPenserPaymentMethod(models.Model):
    """
    Payment Methods Model

    Description:
    Sets up database table for recording payment methods
    """

    class Meta:
        verbose_name_plural = "PaymentMethodsData"
        db_table = "payment_methods"
        ordering = ("paymethod_name",)

    paymethod_data = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ashpenser_data = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="payment_methods")
    paymethod_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return a string representation of this object"""

        return f"{self.paymethod_name}"
    
    def get_absolute_url(self):
        return reverse("apm_categories:apm_paymethod_detail", kwargs={"pk": self.pk})


class ASHPenserPaymentMethodFilter(django_filters.FilterSet):
    """
    Create Filter
    
    Description:
    Provides filter capability for Payment Method Data
    """

    class Meta:
        model = ASHPenserPaymentMethod
        fields = ["paymethod_name",]