from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.tasks.models import Task
from apps.projects.models import Project


class TaskDetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "role"
        )


class TaskDetailProjectSerializer(serializers.ModelSerializer):
    owner = TaskDetailUserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "owner"
        )


class TaskDetailSerializer(serializers.ModelSerializer):
    project = TaskDetailProjectSerializer(read_only=True)
    created_by = TaskDetailUserSerializer(read_only=True)
    assigned_to = TaskDetailUserSerializer(read_only=True)

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
