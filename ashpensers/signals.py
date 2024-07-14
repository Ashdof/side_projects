""" Module to create signals """

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model

from ashpensers.models import ASHPensersProfile

User = get_user_model()

@receiver(post_save, sender=User)
def create_ashpensers_profile(sender, instance, created, **kwargs):

    if created:
        ASHPensersProfile.objects.create(ashpenser=instance)

@receiver(post_save, sender=User)
def save_ashpensers_profile(sender, instance, **kwargs):
    instance.ashpensersprofile.save()

@receiver(pre_delete, sender=User)
def delete_ashpensers_profile(sender, instance, **kwargs):
    try:
        instance.ashpensersprofile.delete()
        print(f"{instance} profile deleted")
    except:
        print(f"{instance} profile not found")