from django.shortcuts import render
from django.views.generic import View, ListView

from members.models import MembersData
from members.forms import MemberCreateForm


# Create your views here.
class MembersDataDisplayView(ListView):
    """
    Display Member Data

    Description:
    This class creates a view to display all member data objects from the
    database
    """

    model = MembersData
    template_name = "members/members_panel.html"
    context_object_name = "mems"