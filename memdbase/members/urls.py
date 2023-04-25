from django.urls import path

from members.views import MembersDataDisplayView

app_name="members"

urlpatterns = [
    path("members_panel/", MembersDataDisplayView.as_view(), name="members_panel"),
] 