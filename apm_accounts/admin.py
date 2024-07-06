"""
Admin Panel

Description:
Create an administration panel for superuser
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apm_accounts.forms import ASHPenserCreationForm, ASHPenserChangeForm
from apm_accounts.models import ASHPenser


# Register your models here.
class ASHPenserAdminPanel(UserAdmin):
    """
    Customize the admin panel for the super user
    """

    add_form = ASHPenserCreationForm
    form = ASHPenserChangeForm
    model = ASHPenser
    list_display = [
        "lastname",
        "firstname",
        "username",
        "email",
        "security_question",
        "security_answer",
        "image",
        "is_active",
        "is_staff",
    ]

    fieldsets = (
        ("Personal Information", {
            "fields": ("lastname", "firstname",),
            "description": "User's personal information",
        }),
        ("Authentication Information", {
            "fields": ("username", "email",),
            "description": "User's authentication information",
        }),
        ("Security Information", {
            "fields": ("security_question", "security_answer",),
            "description": "User's authentication security query",
        }),
        ("Media", {
            "fields": ("image",),
            "description": "User's profile photo",
        }),
        ("Staff Information", {
            "fields": ("is_staff",),
            "description": "User staff status",
        }),
        ("Miscellaneous", {
            "fields": ("is_active",),
            "description": "Current status of user",
        })
    )

admin.site.site_header = "ASHPense Administration Panel"
admin.site.register(ASHPenser, ASHPenserAdminPanel)
admin.site.unregister(Group)