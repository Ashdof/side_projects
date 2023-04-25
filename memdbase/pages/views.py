from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from members.models import MembersData

# Create your views here.
class HomePageView(ListView):
    """
    Display Member Data

    Description:
    This class creates a view to display all member data objects from the
    database
    """

    model = MembersData
    template_name = "index.html"
    context_object_name = "mems"


class MainPageView(TemplateView):
    template_name = "base.html"