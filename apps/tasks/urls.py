from django.urls import path

from apps.tasks.api_endpoints import (
    TaskCreateAPIView,
    TaskListAPIView,
    TaskDetailAPIView,
    TaskAssignedAPIView,
)

app_name = 'tasks'

urlpatterns = [
    path('create', TaskCreateAPIView.as_view(), name='task-create'),
    path("list", TaskListAPIView.as_view(), name='task-list'),
    path("<int:id>", TaskDetailAPIView.as_view(), name='task-detail'),
    path('<int:task_id>/assign', TaskAssignedAPIView.as_view(), name="task-assigned"),
]
