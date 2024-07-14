"""
Module to create forms for managing user profile
"""

from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm

from apm_accounts.choices import SECURITY_QUESTIONS
from apm_accounts.models import ASHPenser
from ashpensers.models import ASHPensersProfile


class ASHPenserForm(forms.ModelForm):
    """
    Update Form

    Description:
    Creates a form to enable a user to update authentication
    data
    """

    class Meta:
        model = ASHPenser
        fields = [
            "lastname",
            "firstname",
            "username",
            "email",
            "security_question",
            "security_answer",
        ]


class ASHPenserPasswordChangeForm(PasswordChangeForm):
    """
    Update Password

    Description:
    Creates a form to enable user to update password data
    """

    security_question = forms.ChoiceField(choices=SECURITY_QUESTIONS, required=True, label="Security question")
    security_answer = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Security answer")

    def __init__(self, *args, **kwargs):
        user = kwargs.get("user")
        super().__init__(*args, **kwargs)

        if user:
            self.fields["security_question"].initial = user.security_question
        
        # Override the custom help texts
        self.fields['old_password'].help_text = ""
        self.fields['new_password1'].help_text = ""
        self.fields['new_password2'].help_text = ""
    
    class Meta:
        model = ASHPenser
        fields = ["old_password", "new_password1", "new_password2", "security_qustion", "security_answer",]

class ASHPensersProfileForm(forms.ModelForm):
    """
    Profile Form

    Description:
    Creates a form for updating user profile
    """

    class Meta:
        model = ASHPensersProfile
        fields = ["bio", "image",]


class ASHPensersProfileChangeForm(forms.ModelForm):
    """
    Profile Update Form

    Description:
    Creates a form for updating user profile information
    """

    class Meta:
        model = ASHPensersProfile
        fields = ["bio", "image", ]


class ASHPensersProfilePasswordChangeForm(PasswordChangeForm):
    """
    Password Change Form

    Description:
    Creates a form to enable the currently loggged-in user to
    change password
    """

    security_question = forms.ChoiceField(choices=SECURITY_QUESTIONS, required=True, label="Security question")
    security_answer = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput, label="Security answer")

    def __init__(self, *args, **kwargs):
        user = kwargs.get("user")
        super().__init__(*args, **kwargs)

        if user:
            self.fields["security_question"].initial = user.security_question
        
        # Override the custom help texts
        self.fields['old_password'].help_text = ""
        self.fields['new_password1'].help_text = ""
        self.fields['new_password2'].help_text = ""
    
    def clean_security_answer(self):
        user = self.user
        security_answer = self.cleaned_data.get("security_answer")
        err_msg = "Sorry, security answer is incorrect!"

        if security_answer != user.security_answer:
            raise forms.ValidationError(err_msg)
        
        return security_answer