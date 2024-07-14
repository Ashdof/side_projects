"""
Transactions Admin Module
"""

from django.contrib import admin

from apm_expenses.models import ASHPenserExpenses


# Register your models here.
@admin.register(ASHPenserExpenses)
class ASHPenserExpensesAdmin(admin.ModelAdmin):
    """
    Customise Admin
    
    Description:
    Customize the admin panel for expenses
    """

    list_display = ["amount", "date", "category", "subcategory", "payee", "payment_method", "description", "ashpenser_data"]
    list_filter = ("date", "category", "subcategory", "payee", "payment_method")
    search_fields = ["category", "subcategory", "payee", "payment_method", "amount"]
    fieldsets = (
        ("Period", {
            "fields": ("date", ),
            "description": "Date of transaction",
        }),
        ("Payment", {
            "fields": ("payee", "payment_method", "amount", ),
            "description": "Payment information",
        }),
        ("Details", {
            "fields": ("category", "subcategory", "description", "ashpenser_data"),
            "description": "Expense particulars",
        }),
    )

admin.site.site_header = "Expenditure Administration Section"