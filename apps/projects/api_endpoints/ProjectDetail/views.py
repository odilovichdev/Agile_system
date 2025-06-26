from rest_framework.generics import RetrieveAPIView

from apps.projects.api_endpoints.ProjectDetail.serializers import ProjectDetailSerializer
from apps.projects.models import Project


class ProjectDetailAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer


__all__ = [
    "ProjectDetailAPIView",
]
