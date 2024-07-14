"""
Test Cases Module

Description:
This module contains test cases for the categories app
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from apm_categories.models import (
    ASHPenserCategories,
    ASHPenserSubCategories,
    ASHPenserPaymentMethod
)


# Create your tests here.
class ASHPenserCategoriesTest(TestCase):
    """
    Categories Test Cases

    Description:
    Test cases for the categories feature
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
            paymethod_name="Bank Transfer",
            description="Brief description of payment method",
            ashpenser_data = cls.user,
        )
    
    # Test Cases for Categories Feature
    def test_categories_model(self):
        """
        Test case for the categories model
        """

        self.assertEqual(self.category.category_name, "Categories")
        self.assertEqual(self.category.category_type, "Type")
        self.assertEqual(self.category.description, "Brief description of category")
        self.assertEqual(self.category.ashpenser_data, self.user)
        self.assertEqual(self.category.get_absolute_url(), "/apm_categories/apm_category_detail/"+str(self.category.pk))
    
    def test_categories_createview(self):
        """Test case for creating new category"""

        response = self.client.post(
            reverse("apm_categories:apm_category_new"),
            {
                "category_name": "Categories",
                "category_type": "Type",
                "description": "Brief description of category",
                "ashpenser_data": self.category.ashpenser_data
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ASHPenserCategories.objects.last().category_name, "Categories")
        self.assertEqual(ASHPenserCategories.objects.last().category_type, "Type")
        self.assertEqual(ASHPenserCategories.objects.last().description, "Brief description of category")


    # Test Cases for Sub-categories Feature
    def test_subcategories_model(self):
        """
        Test case for the sub-categories model
        """

        self.assertEqual(self.subcategory.subcategory_name, "Subcategories")
        self.assertEqual(self.subcategory.category_data, self.category)
        self.assertEqual(self.subcategory.subcategory_type, "Type")
        self.assertEqual(self.subcategory.description, "Brief description of subcategory")
        self.assertEqual(self.subcategory.ashpenser_data, self.user)
        self.assertEqual(self.subcategory.get_absolute_url(), "/apm_categories/apm_subcategory_detail/"+str(self.subcategory.pk))
    
    def test_subcategories_createview(self):
        """Test case for creating new sub-category"""

        response = self.client.post(
            reverse("apm_categories:apm_subcategory_new"),
            {
                "subcategory_name": "Subcategories",
                "category_data": self.subcategory.category_data,
                "subcategory_type": "Type",
                "description": "Brief description of subcategory",
                "ashpenser_data": self.subcategory.ashpenser_data
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ASHPenserSubCategories.objects.last().subcategory_name, "Subcategories")
        self.assertEqual(ASHPenserSubCategories.objects.last().category_data, self.subcategory.category_data)
        self.assertEqual(ASHPenserSubCategories.objects.last().subcategory_type, "Type")
        self.assertEqual(ASHPenserSubCategories.objects.last().description, "Brief description of subcategory")
    

    # Test Cases for Payment Method Feature
    def test_paymentmethod_model(self):
        """
        Test case for the payment method model
        """

        self.assertEqual(self.paymethod.paymethod_name, "Bank Transfer")
        self.assertEqual(self.paymethod.description, "Brief description of payment method")
        self.assertEqual(self.paymethod.ashpenser_data, self.user)
        self.assertEqual(self.paymethod.get_absolute_url(), "/apm_categories/apm_paymethod_detail/"+str(self.paymethod.pk))
    
    def test_subcategories_createview(self):
        """Test case for creating new pyament method"""
        
        response = self.client.post(
            reverse("apm_categories:apm_paymethod_new"),
            {
                "paymethody_name": "Bank Transfer",
                "description": "Brief description of payment method",
                "ashpenser_data": self.paymethod.ashpenser_data
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ASHPenserPaymentMethod.objects.last().paymethod_name, "Bank Transfer")
        self.assertEqual(ASHPenserPaymentMethod.objects.last().description, "Brief description of payment method")
    