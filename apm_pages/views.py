"""
Static Pages View

Description:
Manages the page switching for static pages
"""

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ASHPenserHomePageView(TemplateView):
    """
    Template for the home page
    """
    
    template_name = "home.html"