from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.tasks.api_endpoints.TaskAssigned.serializers import TaskAssignedSerializer
from apps.tasks.models import Task


class TaskAssignedAPIView(UpdateAPIView):
    serializer_class = TaskAssignedSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    lookup_field = "task_id"

    def get_object(self):
        task_id = self.kwargs.get("task_id")
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise serializers.ValidationError(f"{task_id} bu id bilan task topilmadi.")
        return task

    def check_permissions(self, request):
        super().check_permissions(request)
        task = self.get_object()

        # Faqat Project Manager Task bajaruvchi Developer ni biriktira oladi
        if task.created_by.role != get_user_model().Role.PROJECT_MANAGER:
            raise PermissionDenied("Faqat Project Manager Developer ni taskga biriktira oladi.")

        if task.created_by != request.user:
            raise PermissionDenied("Faqat o'zingiz yaratgan taskga Developer biriktira olasiz.")


__all__ = [
    "TaskAssignedAPIView"
]
