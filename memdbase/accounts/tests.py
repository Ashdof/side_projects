from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.
class SignupPageTest(TestCase):

    def test_urls_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
    

    def test_signupview_name(self):
        response = self.client.get(reverse("accounts:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
    
    def test_signup_form(self):
        response = self.client.post(
            reverse("accounts:signup"),
            {
                "username": "testuser",
                "email": "testuser@me.com",
                "password1": "testuser1",
                "password2": "testuser2",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "admin")
        self.assertEqual(get_user_model().objects.all()[0].email, "admin@me.com")