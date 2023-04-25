from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"


class MainPageView(TemplateView):
    template_name = "base.html"