from django.urls import path

from pages.views import HomePageView, MainPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("", MainPageView.as_view(), name="base"),
]