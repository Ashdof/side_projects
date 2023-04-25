from django.urls import path

from members.views import (
    MembersDataDisplayView,
    MembersDataDetailView,
    MembersDataDeleteView,
    MembersDataUpdateView,
    MembersDataCreateView,
)

app_name="members"

urlpatterns = [
    path("members_panel/", MembersDataDisplayView.as_view(), name="members_panel"),
    path("<uuid:pk>/members_detail", MembersDataDetailView.as_view(), name="members_detail"),
    path("<uuid:pk>/member_delete>", MembersDataDeleteView.as_view(), name="member_delete"),
    path("<uuid:pk>/member_update", MembersDataUpdateView.as_view(), name="member_update"),
    path("member_new/", MembersDataCreateView.as_view(), name="member_new"),
] 