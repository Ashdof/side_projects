"""
Model Specifications

Description:
This module specifies the models for APM users
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid
import datetime

from apm_accounts.choices import *


# Create your models here.
class ASHPenser(AbstractUser):
    """
    Custom Fields for Users

    Description:
    This class specifies custom fields to define a database model
    for users

    """

    penser_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    security_question = models.CharField(max_length=255, choices=SECURITY_QUESTIONS, null=True, blank=True)
    security_answer = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(default="default/default.png", upload_to="apmenser/", max_length=255, null=True, blank=True)
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        """
        Rturn a string representation of this user
        """

        return f"{self.last_name} {self.first_name}"