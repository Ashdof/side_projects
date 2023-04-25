from django.db import models

import uuid
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField

from members.choices import GENDER


# Create your models here.
class MembersData(models.Model):
    """
    Member Model Class
    """

    member_data = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(verbose_name="last name", max_length=50)
    first_name = models.CharField(verbose_name="first name", max_length=50)
    gender = models.CharField(verbose_name="gender", max_length=8, choices=GENDER)
    date_of_birth = models.DateField(verbose_name="birth date", max_length=8)
    age = models.PositiveIntegerField(verbose_name="age")
    postal_address = models.CharField(verbose_name="postal address", max_length=50, null=True, blank=True)
    email_address = models.EmailField(verbose_name="email address", null=True, blank=True)
    phone_number = PhoneNumberField(verbose_name="phone number", null=True, blank=True)
    created_at = models.DateField(verbose_name="current date", max_length=8)
    updated_at = models.DateField(default=date.today)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(default="default/default.png", upload_to="members/", null=True, blank=True)

    class Meta:
        verbose_name_plural = "MembersData"
        db_table = "members_data"
        ordering = ("last_name",)

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"
    
    def __str__(self):
        return self.get_full_name()
    