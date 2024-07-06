"""
User Profile URL Module
"""

from django.urls import path

from ashpensers.views import (
    ASHPensersProfilePanelView,
    ASHPensersProfileDeleteView,
    ASHPensersPasswordChangeView,
    ASHPensersProfileUpdateView,
)


app_name="apm_mensers"

urlpatterns = [
    path("apm_mensers/", ASHPensersProfilePanelView.as_view(), name="apm_mensers_panel"),
    path("apm_mensers_delete/<uuid:pk>", ASHPensersProfileDeleteView.as_view(), name="apm_mensers_delete"),
    path("apm_mensers_password_change/<uuid:pk>", ASHPensersPasswordChangeView.as_view(), name="apm_mensers_password_change"),
    path("apm_mensers_update/<uuid:pk>", ASHPensersProfileUpdateView.as_view(), name="apm_mensers_update"),
]
