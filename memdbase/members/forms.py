from django import forms

from members.models import MembersData


class MemberCreateForm(forms.ModelForm):
    """
    Member Data Form Fields

    Description:
    This class defines the member data form fields
    """

    class Meta:
        model = MembersData
        fields = {
            "created_at",
            "last_name",
            "first_name",
            "gender",
            "date_of_birth",
            "age",
            "postal_address",
            "email_address",
            "phone_number",
            "image",
        }