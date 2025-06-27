from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.tasks.api_endpoints.TaskCreate.serializers import TaskCreateSerializer
from apps.tasks.models import Task


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskCreateSerializer


__all__ = [
    "TaskCreateAPIView",
]
