from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.
class CustomUserAdminPanel(UserAdmin):
    """Customise admin panel for admin user"""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "last_name",
        "first_name",
        "date_of_birth",
        "age",
        "image",
    ]

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("date_of_birth", "age", "image",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("date_of_birth", "age", "image",)}),)

    list_filter = ("last_name", "first_name", "age")
    ordering = ("last_name", "first_name", "age")
    search_fields = ("last_name", "first_name", "age", "username")

admin.site.site_header = "Members Database Administration"
admin.site.register(CustomUser, CustomUserAdminPanel)