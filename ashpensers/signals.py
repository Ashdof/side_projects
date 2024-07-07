"""Module to create signals"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from apm_accounts.models import ASHPenser


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        ASHPenser.objects.create(ashpenser=instance)