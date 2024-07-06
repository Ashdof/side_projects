"""
Module for user profile
"""

from django.db import models
from django.conf import settings

from apm_accounts.choices import SECURITY_QUESTIONS

# Create your models here.
class ASHPensersProfile(models.Model):
    """
    Create Profile

    Description:
    Creates a profile for the user upon registration
    """

    class Meta:
        verbose_name_plural = "ASHPensersProfile"
        db_table = "ashpensers_profiles"
        ordering = ("lastname", "firstname",)

    ashpenser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    security_question = models.CharField(max_length=255, choices=SECURITY_QUESTIONS, null=True, blank=True)
    security_answer = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(default="default/default.png", upload_to="apmenser/", max_length=255)
    mfa = models.BooleanField(default=False)

    def __str__(self):
        """ Returns the username of this user """

        return self.ashpenser.username