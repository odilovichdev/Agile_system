from rest_framework.generics import RetrieveAPIView

from apps.tasks.api_endpoints.TaskDetail.serializers import TaskDetailSerializer
from apps.tasks.models import Task


class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    lookup_field = "id"


__all__ = [
    "TaskDetailAPIView"
]
