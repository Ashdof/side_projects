"""
Static Pages View

Description:
Manages the page switching for static pages
"""

from itertools import chain
from decimal import Decimal
from operator import attrgetter
from django.db.models import Sum
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.contrib.auth.mixins import LoginRequiredMixin

from apm_earnings.models import ASHPenserEarnings
from apm_expenses.models import ASHPenserExpenses


# Create your views here.
class ASHPenserDashboardView(LoginRequiredMixin, TemplateView):
    """
    Template for the dashboard page
    """
    
    template_name = "home.html"
    login_url = "login"

    def get_context_data(self, **kwargs):
        """
        Fetch objects from earnings and expenses models
        """

        context = super().get_context_data(**kwargs)
        earnings = ASHPenserEarnings.objects.filter(ashpenser_data=self.request.user)
        expenses = ASHPenserExpenses.objects.filter(ashpenser_data=self.request.user)

        # combine objects and sort by date
        objs = sorted(
            chain(earnings, expenses),
            key=attrgetter("date")
        )

        total_earnings = earnings.aggregate(total=Sum("amount"))["total"] or Decimal("0")
        total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or Decimal("0")
        balance = total_earnings - total_expenses

        context["transactions"] = objs
        context["earnings"] = earnings
        context["expenses"] = expenses
        context["total_earnings"] = total_earnings
        context["total_expenses"] = total_expenses
        context["balance"] = balance

        return context

    @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True))
    def dispatch(self, *args, **kwargs):
        """
        Diasble Cache

        Description:
        Disables the caching of the dashboard by overrding the dispatch
        method. This enforces users to login before accessing the dashboard
        """
        return super().dispatch(*args, **kwargs)


class ASHPenserIndexPageView(TemplateView):
    """
    Template for index/landing page
    """

    template_name = "index.html"