"""
Forms
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = {
            "email",
            "username",
            "last_name",
            "first_name",
            "date_of_birth",
            "age",
            "image",
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = {
            "email",
            "username",
            "last_name",
            "first_name",
            "date_of_birth",
            "age",
            "image",
        }