from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.projects.models import Project


class ProjectDeleteAPIView(DestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("Siz faqat o'zingiz yaratgan projectni o'chira olasiz.")

        instance.delete()


__all__ = [
    "ProjectDeleteAPIView",
]
