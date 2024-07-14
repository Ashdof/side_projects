"""
Transactions Admin Module
"""

from django.contrib import admin

from apm_earnings.models import ASHPenserEarnings


# Register your models here.
@admin.register(ASHPenserEarnings)
class ASHPenserEarningsAdmin(admin.ModelAdmin):
    """
    Customise Admin
    
    Description:
    Customize the admin panel for income earnings
    """

    list_display = ["amount", "date", "category", "payer", "payment_method", "description", "ashpenser_data"]
    list_filter = ("date", "category", "payer", "payment_method")
    search_fields = ["category", "payer", "payment_method", "amount"]
    fieldsets = (
        ("Period", {
            "fields": ("date", ),
            "description": "Date of transaction",
        }),
        ("Payment", {
            "fields": ("payer", "payment_method", "amount", ),
            "description": "Payment information",
        }),
        ("Details", {
            "fields": ("category", "description", "ashpenser_data"),
            "description": "Income particulars",
        }),
    )

admin.site.site_header = "Income Earnings Administration Section"