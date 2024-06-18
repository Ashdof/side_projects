"""
Form Fields

Description:
This module specifies the in-built form elements for
gathering data about users
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
            "last_name",
            "first_name",
            "security_question",
            "security_answer",
            "image",
        )


class ASHPenserChangeForm(UserChangeForm):
    """
    Update User Data

    Description:
    This class creates a form for updating the data of a user
    """

    class Meta:
        model = ASHPenser
        fields = (
            "username",
            "email",
            "last_name",
            "first_name",
            "security_question",
            "security_answer",
            "image",
        )