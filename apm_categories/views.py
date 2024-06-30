"""
ASHPense Categories View
"""

from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models.base import Model as Model
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apm_categories.models import (
    ASHPenserCategories,
    ASHPenserSubCategories,
    ASHPenserPaymentMethod
)


# Create your views here.
class ASHPenserCategoryListView(LoginRequiredMixin, TemplateView):
    """
    Categories List View

    Description:
    Creates a view for the display of categories list
    """

    # model = ASHPenserCategories
    template_name = "apm_categories/apm_categories_panel.html"

    def get_queryset(self):
        """Filter users"""
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        """
        Get Context Data

        Descriptions:
        Loads data from three models
        """

        context = super().get_context_data(**kwargs)
        context["apm_categories"] = ASHPenserCategories.objects.filter(ashpenser_data=self.request.user)
        context["apm_subcategories"] = ASHPenserSubCategories.objects.filter(ashpenser_data=self.request.user)
        context["apm_paymethods"] = ASHPenserPaymentMethod.objects.filter(ashpenser_data=self.request.user)

        return context


class ASHPenserCategoryDetailView(LoginRequiredMixin, DetailView):
    """
    Display Category Object Details

    Description:
    Displays the details of a selected category object
    """

    model = ASHPenserCategories
    template_name = "apm_categories/details/apm_category_detail.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj


class ASHPenserCategoryUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update Category Object Data

    Description
    Displays form to update data of a category's object
    """

    model = ASHPenserCategories
    fields = ["category_name", "category_type", "description"]
    template_name = "apm_categories/updates/apm_category_update.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj
    


class ASHPenserCategoryDeleteView(DeleteView):
    """
    Delete an Object

    Description:
    Deletes a selected object
    """

    model = ASHPenserCategories
    template_name = "apm_categories/delete/apm_category_delete.html"
    success_url = reverse_lazy("apm_categories:apm_categories_panel")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def get_object(self, queryset=None):
        """Fetch resources by current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj

    def delete(self, request, *args, **kwargs):
        """Delete the selected object"""

        info_msg = "Category data deleted."
        messages.success(request, info_msg)
        return super().delete(request, *args, **kwargs)


class ASHPenserCategoryCreateView(LoginRequiredMixin, CreateView):
    """
    Create Category Object

    Description:
    Creates a new category object
    """

    model = ASHPenserCategories
    template_name = "apm_categories/new/apm_category_new.html"
    fields = (
        "category_name",
        "category_type",
        "description",
    )
    success_url = reverse_lazy("apm_categories:apm_categories_panel")

    def form_valid(self, form):
        """Commit resources to the database by user"""

        form.instance.ashpenser_data = self.request.user
        return super().form_valid(form)


class ASHPenserSubCategoryDetailView(LoginRequiredMixin, DetailView):
    """
    Display Sub-category Object Details

    Description:
    Displays the details of a selected sub-category object
    """

    model = ASHPenserSubCategories
    template_name = "apm_categories/details/apm_subcategory_detail.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj


class ASHPenserSubCategoryUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update Sub-category Object Data

    Description:
    Displays form to update data of subcategory's bject
    """

    model = ASHPenserSubCategories
    fields = ["subcategory_name", "subcategory_type", "category_data",  "description"]
    template_name = "apm_categories/updates/apm_subcategory_update.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj


class ASHPenserSubCategoryDeleteView(DeleteView):
    """
    Delete an Object

    Description:
    Deletes a selected object
    """

    model = ASHPenserSubCategories
    template_name = "apm_categories/delete/apm_subcategory_delete.html"
    success_url = reverse_lazy("apm_categories:apm_categories_panel")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def get_object(self, queryset=None):
        """Fetch resources by current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj

    def delete(self, request, *args, **kwargs):
        info_msg = "Sub-category data deleted."
        messages.success(request, info_msg)
        return super().delete(request, *args, **kwargs)


class ASHPenserSubCategoryCreateView(LoginRequiredMixin, CreateView):
    """
    Create Sub-category Object

    Description:
    Creates a new sub-category object
    """

    model = ASHPenserSubCategories
    template_name = "apm_categories/new/apm_subcategory_new.html"
    fields = (
        "subcategory_name",
        "category_data",
        "subcategory_type",
        "description",
    )
    success_url = reverse_lazy("apm_categories:apm_categories_panel")

    def form_valid(self, form):
        """Commit resources to the database by user"""

        form.instance.ashpenser_data = self.request.user
        return super().form_valid(form)


class ASHPenserPaymentMethodDetailView(LoginRequiredMixin, DetailView):
    """
    Display Payment method Object Details

    Description:
    Displays the details of a selected sub-category object
    """

    model = ASHPenserPaymentMethod
    template_name = "apm_categories/details/apm_paymethod_detail.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj


class ASHPenserPaymentMethodUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update Payment Method Object Data

    Description:
    Displays form to update data of payment method's object
    """

    model = ASHPenserPaymentMethod
    fields = ["paymethod_name", "description"]
    template_name = "apm_categories/updates/apm_paymethod_update.html"

    def get_object(self, queryset=None):
        """Fetch resources by the current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj


class ASHPenserPaymentMethodDeleteView(DeleteView):
    """
    Delete an Object

    Description:
    Deletes a selected object
    """

    model = ASHPenserPaymentMethod
    template_name = "apm_categories/delete/apm_paymethod_delete.html"
    success_url = reverse_lazy("apm_categories:apm_categories_panel")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def get_object(self, queryset=None):
        """Fetch resources by current logged in user"""

        obj = super().get_object(queryset)
        if obj.ashpenser_data != self.request.user:
            raise Http404("Error: Forbidden")
        
        return obj

    def delete(self, request, *args, **kwargs):
        info_msg = "Payment method data deleted."
        messages.success(request, info_msg)
        return super().delete(request, *args, **kwargs)


class ASHPenserPaymentMethodCreateView(LoginRequiredMixin, CreateView):
    """
    Create Payment Method Object

    Description:
    Creates a new payment method object
    """

    model = ASHPenserPaymentMethod
    template_name = "apm_categories/new/apm_paymethod_new.html"
    fields = (
        "paymethod_name",
        "description",
    )
    success_url = reverse_lazy("apm_categories:apm_categories_panel")

    def form_valid(self, form):
        """Commit resources to the database by user"""

        form.instance.ashpenser_data = self.request.user
        return super().form_valid(form)