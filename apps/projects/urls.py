from django.urls import path

from apps.projects.api_endpoints import (
    ProjectCreateAPIView,
    ProjectDeleteAPIView,
    ProjectListAPIView,
    ProjectDetailAPIView,
    AddMemberAPIView,
)

app_name = "projects"

urlpatterns = [
    path("create/", ProjectCreateAPIView.as_view(), name="project-create"),
    path("list", ProjectListAPIView.as_view(), name='project-list'),
    path("<int:pk>", ProjectDetailAPIView.as_view(), name='project-detail'),
    path("<int:project_id>/add-member", AddMemberAPIView.as_view(), name="project-add-member"),
    path("<int:pk>/delete", ProjectDeleteAPIView.as_view(), name='project-delete'),
]
