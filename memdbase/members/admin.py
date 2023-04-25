from django.contrib import admin

from members.models import MembersData
from members.forms import MemberCreateForm

# Register your models here. 
@admin.register(MembersData)
class MembersDataAdmin(admin.ModelAdmin):
    """Customise admin panel for members data"""

    list_display = (
        "last_name",
        "first_name",
        "gender",
        "date_of_birth",
        "age",
        "postal_address",
        "email_address",
        "phone_number",
        "created_at",
        "updated_at",
        "is_active",
        "image"
    )

    list_filter = ("last_name", "first_name", "gender", "age",)
    ordering = ("last_name", "first_name", "gender", "age", "is_active")
    search_fields = ("last_name", "first_name", "gender", "age")
    fieldsets = (
        (
            "Required information", {
                "description": "These are required fields",
                "fields": ("created_at", "last_name", "first_name", "gender", "date_of_birth", "age")
            }
        ),
        (
            "Optional information", {
                "description": "These are optional fields",
                "fields": ("postal_address", "email_address", "phone_number", "image"),
            }
        )
    )