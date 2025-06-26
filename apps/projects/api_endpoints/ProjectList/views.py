from rest_framework.generics import ListAPIView
from django.db.models import Q, Prefetch

from apps.projects.models import Project, ProjectMembership
from apps.projects.api_endpoints.ProjectList.serializers import ProjectListSerializer


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


__all__ = [
    "ProjectListAPIView",
]
