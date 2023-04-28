from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import View, ListView, DetailView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from members.models import MembersData
from members.forms import MemberCreateForm


# Create your views here.
class MembersDataDisplayView(LoginRequiredMixin, ListView):
    """
    Display Member Data

    Description:
    This class creates a view to display all member data objects from the
    database
    """

    model = MembersData
    template_name = "index.html"
    context_object_name = "mems"


class MembersDataDetailView(LoginRequiredMixin, DetailView):
    """
    Member Detail View

    Description:
    This class fetches and displays the detail of a member object from the
    database

    """

    model = MembersData
    template_name = "members/members_detail.html"
    context_object_name = "mems"


class MembersDataDeleteView(LoginRequiredMixin, DeleteView):
    """
    Member Delete View

    Description:
    This class deletes a member object from the database

    """

    model = MembersData
    template_name = "members/member_delete.html"
    context_object_name = "mems"
    success_url = reverse_lazy("index")


class MembersDataUpdateView(LoginRequiredMixin, UpdateView):
    """
    Member Update View

    Description:
    This class updates the data of a member object in the database

    """

    model = MembersData
    template_name = "members/member_update.html"
    fields = [
        "last_name",
        "first_name",
        "gender",
        "date_of_birth",
        "age",
        "postal_address",
        "email_address",
        "phone_number",
        "is_active",
        "image"
    ]
    success_url = reverse_lazy("index")


class MembersDataCreateView(LoginRequiredMixin, CreateView):
    """
    Create New Member Object

    Description:
    This class creates a new member object

    """

    model = MembersData
    fields = [
        "created_at",
        "last_name",
        "first_name",
        "gender",
        "date_of_birth",
        "age",
        "postal_address",
        "email_address",
        "phone_number",
        "image"
    ]
    template_name = "members/member_new.html"
    success_url = reverse_lazy("members:member_new")


class MembersDataSearchView(LoginRequiredMixin, ListView):
    """
    Member Search View

    Description:
    This class searches for a specified member object

    """

    model = MembersData
    template_name = "members/member_search.html"

    def get_queryset(self):
        qs = super().get_queryset()
        search_term = self.request.GET.get("q")

        if search_term:
            qs = qs.filter(
                Q(last_name__icontains=search_term) |
                Q(first_name__icontains=search_term) |
                Q(age__icontains=search_term) |
                Q(gender__icontains=search_term)
            )
        
        return qs 