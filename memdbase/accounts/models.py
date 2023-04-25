from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid
import datetime

# Create your models here.
class CustomUser(AbstractUser):
    user_data = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField(verbose_name="birth date of user", max_length=8, null=True, blank=True)
    age = models.PositiveIntegerField(verbose_name="age of user", null=True, blank=True)
    image = models.ImageField(default="default/default.png", upload_to="users/", null=True, blank=True)

    @property
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"
    
    def __str__(self):
        return self.get_full_name