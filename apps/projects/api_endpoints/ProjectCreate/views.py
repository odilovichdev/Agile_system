from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.projects.api_endpoints.ProjectCreate.serializers import ProjectCreateSerializer
from apps.projects.models import Project


class ProjectCreateAPIView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


__all__ = [
    "ProjectCreateAPIView",
]
