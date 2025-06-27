from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.tasks.models import Task
from apps.projects.models import Project


class TaskListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "role"
        )


class TaskListProjectSerializer(serializers.ModelSerializer):
    owner = TaskListUserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "owner"
        )


class TaskListSerializer(serializers.ModelSerializer):
    project = TaskListProjectSerializer(read_only=True)
    created_by = TaskListUserSerializer(read_only=True)
    assigned_to = TaskListUserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "project",
            "created_by",
            "assigned_to"
        )
