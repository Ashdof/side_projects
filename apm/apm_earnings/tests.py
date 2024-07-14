"""
Test Cases Module

Description:
This module contains test cases for the earnings app
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from apm_categories.models import ASHPenserCategories, ASHPenserPaymentMethod
from apm_earnings.models import ASHPenserEarnings


# Create your tests here.
class ASHPenserEarningsTest(TestCase):
    """
    Earnings Test Cases

    Description:
    Test cases for the earnings feature
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

        # payment method feature setup
        cls.paymethod = ASHPenserPaymentMethod.objects.create(
            paymethod_name="Bank Transfer",
            description="Brief description of payment method",
            ashpenser_data = cls.user,
        )
        
        # earnings feature setup
        cls.earnings = ASHPenserEarnings.objects.create(
            date="2024-04-23",
            category=cls.category,
            payer="My Employer",
            payment_method=cls.paymethod,
            amount=4500.00,
            description="Brief description of earning for the period",
            ashpenser_data = cls.user,
        )

    
    # Test Cases for Categories Feature
    def test_earnings_model(self):
        """
        Test case for the earnings model
        """

        self.assertEqual(self.earnings.date, "2024-04-23")
        self.assertEqual(self.earnings.category, self.category)
        self.assertEqual(self.earnings.payer, "My Employer")
        self.assertEqual(self.earnings.payment_method, self.paymethod)
        self.assertEqual(self.earnings.amount, 4500.00)
        self.assertEqual(self.earnings.description, "Brief description of earning for the period")
        self.assertEqual(self.earnings.ashpenser_data, self.user)
        self.assertEqual(self.earnings.get_absolute_url(), "/apm_earnings/apm_earnings_detail/"+str(self.earnings.pk))
    
    def test_earnings_createview(self):
        """Test case for creating new earnings"""

        response = self.client.post(
            reverse("apm_earnings:apm_earnings_new"),
            {
                "date": "2024-04-23",
                "category": self.category,
                "payer": "My Employer",
                "payment_method": self.paymethod,
                "amount": 4500.00,
                "description": "Brief description of earning for the period",
                "ashpenser_data": self.category.ashpenser_data
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ASHPenserEarnings.objects.last().date, "2024-04-23")
        self.assertEqual(ASHPenserEarnings.objects.last().category, self.category)
        self.assertEqual(ASHPenserEarnings.objects.last().payer, "My Employer")
        self.assertEqual(ASHPenserEarnings.objects.last().payment_method, self.paymethod)
        self.assertEqual(ASHPenserEarnings.objects.last().amount, 4500.00)
        self.assertEqual(ASHPenserEarnings.objects.last().description, "Brief description of earning for the period")
