from django.urls import path

from accounts.views import (
    SignupView,
    ProfileView,
    ProfileUpdateView,
    ProfilePasswordChangeView,
    ProfilePasswordChangeDoneView,
)


app_name = "accounts"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("profile/<str:username>", ProfileView.as_view(), name="profile"),
    path("profile_update/<str:username>", ProfileUpdateView.as_view(), name="profile_update"),
    path("password_change/", ProfilePasswordChangeView.as_view(), name="password_change"),
    path("password_change_done/", ProfilePasswordChangeDoneView.as_view(), name="password_change_done"),
]