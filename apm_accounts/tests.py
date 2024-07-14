"""
Test Cases for the APM Accounts
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from apm_accounts.models import ASHPenser


# Create your tests here.
class ASHPenserSignupTest(TestCase):
    """
    Test cases for sign up view
    """

    def test_url_exists_at_correct_location(self):
        """
        Test for the existence of the url at the correct location
        """

        response = self.client.get("/apm_accounts/signup/")
        self.assertEqual(response.status_code, 200)
    
    def test_signup_view_name(self):
        """
        Test for the signup view name and the correct template
        """

        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
    
    def test_signup_form(self):
        """
        Test the signup form
        """

        response = self.client.post(
            reverse("signup"), 
            {
                "username": "testuser",
                "email": "testuser@me.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@me.com")
    
    def test_signup_form_with_missing_field(self):
        """
        Test signup form with invalid data
        """

        response = self.client.post(
            reverse("signup"), 
            {
                "username": "testuser",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
    
    def test_register_user_with_invalid_email(self):
        """Test case for signup with invalid email"""

        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "invalidemail",
                "password1": "TestPassword123",
                "password2": "TestPassword123"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address")
    
    def test_register_user_with_invalid_username(self):
        """Test case for signup with invalid username"""

        response = self.client.post(
            reverse("signup"),
            {
                "username": "printfguy",
                "email": "testuser@me.com",
                "password1": "testpass123",
                "password2": "testpass123",
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response, "Please enter a correct username.")


class ASHPenserLoginTest(TestCase):
    """
    Test cases for user login
    """

    def setUp(self):
        self.user = ASHPenser.objects.create_user(
            username="testuser",
            password="TestPassword123"
        )
    
    def test_login_with_valid_credentials(self):
        """Test case for valid user credentials"""

        response = self.client.post(
            reverse("login"), {
            "username": "testuser",
            "password": "TestPassword123"
        })

        self.assertEqual(response.status_code, 302)
    
    def test_login_with_invalid_credentials(self):
        """Test case for invalid user credentials"""

        response = self.client.post(
            reverse("login"),
            {
                "username": "testuser",
                "password": "WrongPassword"
            }
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password.')