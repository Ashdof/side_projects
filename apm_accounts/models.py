"""
Model Specifications

Description:
This module specifies the models for APM users
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid
import datetime

from apm_accounts.choices import SECURITY_QUESTIONS


# Create your models here.
class ASHPenser(AbstractUser):
    """
    Custom Fields for Users

    Description:
    This class specifies custom fields to define a database model
    for users

    """

    class Meta:
        verbose_name_plural = "ASHPenserAdmin"
        db_table = "ashpenser_admin"
        ordering = ("username",)

    penser_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    security_question = models.CharField(max_length=255, choices=SECURITY_QUESTIONS, null=True, blank=True)
    security_answer = models.CharField(max_length=500, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        """
        Rturn a string representation of this user
        """

        return self.username


