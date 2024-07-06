"""
Admin panel for user profile
"""

from django.contrib import admin

# from ashpensers.models import ASHPensersProfile
from apm_accounts.models import ASHPenser
from ashpensers.forms import ASHPensersProfileForm, ASHPensersProfileChangeForm

# Register your models here.
class ASHPensersProfileAdminPanel(admin.ModelAdmin):
    """
    Customize the admin panel for users profile
    """

    add_form = ASHPensersProfileForm
    form = ASHPensersProfileChangeForm
    nodel = ASHPenser
    list_display = [
        "lastname",
        "firstname",
        "security_question",
        "security_answer",
        "image",
    ]

    fieldsets = (
        ("Personal Information", {
            "fields": ("lastname", "firstname"),
            "description": "User's personal information",
        }),
        ("Security Information", {
            "fields": ("security_question", "security_answer"),
            "description": "User authentication security information",
        }),
        ("Media", {
            "fields": ("image",),
            "description": "Profile photo of user",
        })
    )


admin.site.site_header = "ASHPensers Profile Section"