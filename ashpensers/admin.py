"""
Admin panel for user profile
"""

from django.contrib import admin

from ashpensers.models import ASHPensersProfile
from ashpensers.forms import ASHPensersProfileForm, ASHPensersProfileChangeForm

# Register your models here.
@admin.register(ASHPensersProfile)
class ASHPensersProfileAdminPanel(admin.ModelAdmin):
    """
    Customize the admin panel for users profile
    """

    add_form = ASHPensersProfileForm
    form = ASHPensersProfileChangeForm
    moodel = ASHPensersProfile
    list_display = [
        "bio",
        "image",
    ]

    fieldsets = (
        ("Bio Information", {
            "fields": ("bio",),
            "description": "User's about information",
        }),
        ("Media", {
            "fields": ("image",),
            "description": "Profile photo of user",
        })
    )


admin.site.site_header = "ASHPensers Profile Section"