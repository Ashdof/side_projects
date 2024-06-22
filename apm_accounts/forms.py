"""
Form Module

Description:
This module specifies the in-built and custom form elements for
gathering data about users
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from apm_accounts.models import ASHPenser


class ASHPenserCreationForm(UserCreationForm):
    """
    Create New User

    Description:
    This class creates a form for the resgistration of new users
    """

    class Meta(UserCreationForm):
        model = ASHPenser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
    
    def clean_ashpenser_username(self):
        """
        Unique Username

        Description:
        This method eliminates duplicate usernames. It prompts the user for
        an attempt to provide a duplicate username
        
        Returns:
        The username
        """

        username = self.clean_data.get("username")
        err_msg = f"{username} already taken.\nPlease choose a different username."

        if ASHPenser.objects.filter(username=username).exists():
            raise forms.ValidationError(err_msg)
        
        return username


class ASHPenserChangeForm(UserChangeForm):
    """
    Update User Data

    Description:
    This class creates a form for updating the data of a user
    """

    class Meta:
        model = ASHPenser
        fields = (
            "last_name",
            "first_name",
            "username",
            "email",
            "security_question",
            "security_answer",
            "image",
        )


class ASHPenserLoginForm(forms.Form):
    """
    Login User

    Description:
    This class creates a custom login feature to authenticate users
    """

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)