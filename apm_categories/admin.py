"""
Categories Admin Module
"""

from django.contrib import admin

from apm_categories.models import ASHPenserCategories


# Register your models here.
@admin.register(ASHPenserCategories)
class ASHPenserCategoriesAdmin(admin.ModelAdmin):
    """
    Customise Admin
    
    Description:
    Customises the admin panel for categories
    """

    list_display = ["category_name", "category_type", "date_created", "description", "ashpenser_data"]
    list_filter = ("category_name", "category_type", "date_created",)
    search_fields = ["category_name",]
    fieldsets = (
        ("Period", {
            "fields": ("date_created", ),
            "description": "Date and time for creating category",
        }),
        ("Category Particulars", {
            "fields": ("category_name", "category_type", "description", "ashpenser_data",),
            "description": "Category details",
        }),
    )

admin.site.site_header = "Categories Administration Section"