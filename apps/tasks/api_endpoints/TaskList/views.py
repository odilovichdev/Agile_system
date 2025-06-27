from rest_framework.generics import ListAPIView

from apps.tasks.models import Task
from apps.tasks.api_endpoints.TaskList.serializers import TaskListSerializer


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


__all__ = [
    "TaskListAPIView"
]
