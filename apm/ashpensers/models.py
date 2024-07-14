"""
Module for user profile
"""

from django.db import models
from django.conf import settings

from PIL import Image

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

    ashpenser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(default="default/default.png", upload_to="apmenser/", max_length=255)

    def __str__(self):
        """ Returns the username of this user """

        return f"{ self.ashpenser.username }"
    
    def save(self, *args, **kwargs):
        """
        Save Profile Object

        Description:
        Commits this user's profile object to the database
        """

        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            img_size = (300, 280)
            img.thumbnail(img_size)
            img.save(self.image.path)