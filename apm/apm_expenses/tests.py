"""
Test Cases Module

Description:
This module contains test cases for the expense app
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from apm_expenses.models import ASHPenserExpenses
from apm_categories.models import (
    ASHPenserCategories,
    ASHPenserPaymentMethod,
    ASHPenserSubCategories,
)



# Create your tests here.
class ASHPenserEarningsTest(TestCase):
    """
    Expenses Test Cases

    Description:
    Test cases for the expenses feature
    """

    @classmethod
    def setUpTestData(cls):
        """Setup data for testing"""

        # User setup
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@me.com",
            password="secret"
        )

        # categories feature setup
        cls.category = ASHPenserCategories.objects.create(
            category_name="Categories",
            category_type="Type",
            description="Brief description of category",
            ashpenser_data = cls.user,
        )

        # sub-categories feature setup
        cls.subcategory = ASHPenserSubCategories.objects.create(
            subcategory_name="Subcategories",
            category_data=cls.category,
            subcategory_type="Type",
            description="Brief description of subcategory",
            ashpenser_data = cls.user,
        )

        # payment method feature setup
        cls.paymethod = ASHPenserPaymentMethod.objects.create(
            paymethod_name="Cash",
            description="Brief description of payment method",
            ashpenser_data = cls.user,
        )
        
        # expenses feature setup
        cls.expenses = ASHPenserExpenses.objects.create(
            date="2024-07-01",
            category=cls.category,
            subcategory=cls.subcategory,
            payee="Provisions shop",
            payment_method=cls.paymethod,
            amount=8.00,
            description="Purchased a loaf of bread",
            ashpenser_data = cls.user,
        )

    
    # Test Cases for Expenses Feature
    def test_expenses_model(self):
        """
        Test case for the expenses model
        """

        self.assertEqual(self.expenses.date, self.expenses.date)
        self.assertEqual(self.expenses.category, self.category)
        self.assertEqual(self.expenses.subcategory, self.subcategory)
        self.assertEqual(self.expenses.payee, "Provisions shop")
        self.assertEqual(self.expenses.payment_method, self.paymethod)
        self.assertEqual(self.expenses.amount, 8.00)
        self.assertEqual(self.expenses.description, "Purchased a loaf of bread")
        self.assertEqual(self.expenses.ashpenser_data, self.user)
        self.assertEqual(self.expenses.get_absolute_url(), "/apm_expenses/apm_expenses_detail/"+str(self.expenses.pk))
    
    def test_expenses_createview(self):
        """Test case for creating new expenses"""

        response = self.client.post(
            reverse("apm_expenses:apm_expenses_new"),
            {
                "date": "2024-07-01",
                "category": self.category,
                "subcategory": self.subcategory,
                "payee": "Provisions shop",
                "payment_method": self.paymethod,
                "amount": 8.00,
                "description": "Purchased a loaf of bread",
                "ashpenser_data": self.category.ashpenser_data
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ASHPenserExpenses.objects.last().date, self.expenses.date)
        self.assertEqual(ASHPenserExpenses.objects.last().category, self.category)
        self.assertEqual(ASHPenserExpenses.objects.last().category, self.subcategory)
        self.assertEqual(ASHPenserExpenses.objects.last().payer, "Provisions shop")
        self.assertEqual(ASHPenserExpenses.objects.last().payment_method, self.paymethod)
        self.assertEqual(ASHPenserExpenses.objects.last().amount, 8.00)
        self.assertEqual(ASHPenserExpenses.objects.last().description, "Purchased a loaf of bread")
