from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import View, CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
class SignupView(CreateView):
    """Sign up view"""

    form_class = CustomUserCreationForm 
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class ProfileView(View):
    """
    Profile View

    Description:
    This class renders the profile information of the user

    """

    def post(self, request, *args, **kwargs):
        username = kwargs.get('username')
        user = get_user_model().objects.filter(username=username).first()
        if not user:
            return redirect("index")

        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile", username=username)
        else:
            return render(request, "profile/profile_update.html", context={"form": form})


    def get(self, request, *args, **kwargs): 
        username = kwargs.get('username')
        user = get_user_model().objects.filter(username=username).first()
        if user:
            form = CustomUserChangeForm(instance=user)
            return render(request, "profile/profile.html", context={"form": form})
        return redirect("index")


class ProfileUpdateView(UpdateView):
    """
    Update Profile View

    Description:
    This class enables the signed in user to update his or her profile information
    """

    def post(self, request, *args, **kwargs):
        username = kwargs.get('username')
        user = get_user_model().objects.filter(username=username).first()
        
        if user:
            form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                return redirect("accounts:profile", username=username)
            else:
                return render(request, "profile/profile.html", context={"form": form})


    def get(self, request, *args, **kwargs): 
        username = kwargs.get('username')
        user = get_user_model().objects.filter(username=username).first()
        if user:
            form = CustomUserChangeForm(instance=user)
            return render(request, "profile/profile_update.html", context={"form": form})
        return redirect("index")

class ProfilePasswordChangeView(View):
    """
    Password Change View

    Description:
    This class enables the user to change his or her password

    """

    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        return render(request, "registration/password_change_form.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("password_change_done")
        else:
            messages.error(request, "Please correct the messages below")
        
        return render(request, "registration/password_change_form.html", {"form": form})


class ProfilePasswordChangeDoneView(View):
    """
    Password Change Done View

    Description:
    This class presents the view for password change done

    """

    def get(self, request, *args, **kwargs):
        return render(request, "registration/password_change_done.html")